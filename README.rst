**WARNING: this project is not maintained**

################
Django Navigator
################

A little module that let you navigate from DetailView to DetailView
with previous and next button from a ListView or a SearchView.


USAGE
=====

Create your own **navigator.py**::

    import navigator
    from myapp.models import Document


    class DocumentNavigator(navigator.Navigator):
        session_id = 'document_navigator_ids'
        url_id = 'my_app:document_preview'
    
        def __init__(self, current_doc_id, owner):
            queryset = Document.objects.of(owner).order_by('created_at')
            super(DocumentNavigator, self).__init__(current_doc_id, queryset)



In the **views.py**::

    from django.views.generic import DetailView
    from myapp.models import Document
    from myapp.navigator import DocumentNavigator

    class DocumentPreview(DetailView):
        """Display the preview of the document"""
        template_name = "my_app/document_preview.html"
        model = Document
        slug_field = 'uuid'
    
        def get_queryset(self):
            queryset = super(DocumentPreview, self).get_queryset()
            return queryset.of(self.request.user)
    
        def get_context_data(self, **kwargs):
            data = super(DocumentPreview, self).get_context_data(**kwargs)
            data['navigator'] = DocumentNavigator(obj.uuid, self.request.user)
            data['navigator'].set_ids(self.request.session)
            return data


In the **template.html**::

    {% if navigator.previous or navigator.next %}
        <div class="document_navigator">
             <a {% if navigator.previous %}href="{{ navigator.previous_url }}" {% endif %}class="btn btn-primary btnback{% if not navigator.previous %} disabled{% endif %}"><i class="icon-arrow-left"></i> </a>
             <a {% if navigator.next %}href="{{ navigator.next_url }}" {% endif %}class="btn btn-primary btnforward{% if not navigator.next %} disabled{% endif %}"> <i class="icon-arrow-right"></i></a>
            <div class="spacer">&nbsp;</div>
        </div>
    {% endif %}


Then you have previous and next buttons in you DetailView and that's it !
