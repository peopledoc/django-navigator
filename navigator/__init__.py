# -*- coding: utf-8 -*-
"""A Navigator that let you navigate in a QuerySet from object DetailView.

"""
from django.db import models


class Navigator(object):
    """
    Navigate in a queryset with next and previous links.
    """
    session_id = None
    url_id = None
    id_field_name = 'pk'

    def __init__(self, current_id, queryset):
        self.current_id = str(current_id)
        self.queryset = queryset

    @property
    def ids(self):
        """
        Get ids of queryset
        """
        if not hasattr(self, '_ids_cache'):
            setattr(self, '_ids_cache',
                    list(self.queryset.values_list(
                        self.id_field_name, flat=True)))
        return self._ids_cache

    def set_ids(self, session):
        """
        Set _ids_cache, so next and previous use given id list instead
        of all ids.
        """
        ids = session.get(self.session_id, [])
        if ids:
            # Be sure each id from ids exists in queryset
            qs_ids = list(self.queryset.filter(pk__in=ids).values_list(
                self.id_field_name, flat=True))
            # Keep order of original ids list
            ids = [id for id in ids if id in qs_ids]
            # Set ids in cache
            setattr(self, '_ids_cache', ids)
            return ids
        else:
            return self.ids

    @property
    def first(self):
        if self.ids:
            return self.ids[0]
        return None

    @property
    def last(self):
        if self.ids:
            return self.ids[-1]
        return None

    @property
    def previous(self):
        try:
            if self.ids and self.first != self.current_id:
                index = self.ids.index(self.current_id)
                return self.ids[index - 1]
            return None
        except ValueError:
            return None

    @property
    def next(self):
        try:
            if self.ids and self.last != self.current_id:
                index = self.ids.index(self.current_id)
                return self.ids[index + 1]
            return None
        except ValueError:
            return None

    @models.permalink
    def previous_url(self):
        if self.previous:
            return (self.url_id, [self.previous])
        return None

    @models.permalink
    def next_url(self):
        if self.next:
            return (self.url_id, [self.next])
        return None
