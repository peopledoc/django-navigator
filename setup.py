# -*- coding: utf-8 -*-
"""Python packaging."""
from os.path import abspath, dirname, join
from setuptools import setup


def read_relative_file(filename):
    """Returns contents of the given file, which path is supposed relative
    to this module."""
    with open(join(dirname(abspath(__file__)), filename)) as f:
        return f.read()


name = 'django-navigator'
version = read_relative_file('VERSION').strip()
readme = read_relative_file('README.rst')
requirements = []
entry_points = {}


if __name__ == '__main__':  # ``import setup`` doesn't trigger setup().
    setup(name=name,
          version=version,
          description="""A module that add previous and next """
          """button to a DetailView""",
          long_description=readme,
          classifiers=["Programming Language :: Python",
                       'License :: Other/Proprietary License',
                       ],
          keywords='',
          author=u'Lauréline Guérin',
          author_email='laureline.guerrin@novapost.fr',
          url='https://github.com/novagile/%s' % name,
          license='WTFPL',
          packages=['navigator'],
          include_package_data=True,
          zip_safe=False,
          install_requires=requirements,
          entry_points=entry_points,
          )
