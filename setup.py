from __future__ import absolute_import
import os
from setuptools import setup, find_packages
version = '0.3.3.4'
README = os.path.join(os.path.dirname(__file__), 'README.md')
long_description = open(README).read()
setup(name='django-locking',
      version=version,
      description="Prevents users from doing concurrent editing in Django. Works out of the box in the admin interface, or you can integrate it with your own apps using a public API.",
      long_description=long_description,
      classifiers=['Development Status :: 4 - Beta',
                   'Environment :: Web Environment',
                   'Framework :: Django',
                   'Intended Audience :: Developers',
                   'License :: OSI Approved :: BSD License',
                   'Operating System :: OS Independent',
                   'Programming Language :: Python',
                   'Topic :: Software Development :: Libraries :: Python Modules',
                   'Topic :: Utilities'],
      keywords='locking mutex',
      url='https://github.com/UndercoverTourist/django-locking',
      download_url='https://github.com/UndercoverTourist/django-locking/tarball/master',
      license='BSD',
      packages=find_packages(),
      install_requires=['django-staticfiles', 'simplejson'],
      )
