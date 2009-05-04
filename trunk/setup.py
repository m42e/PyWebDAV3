#!/usr/bin/env python

try: 
   from ez_setup import use_setuptools 
   use_setuptools() 
except ImportError: 
   pass 

from setuptools import setup

VERSION = open('VERSION', 'r').read()
VERSION = VERSION.replace('\n', '')

from distutils.core import setup
setup(name='PyWebDAV',
      description='WebDAV library and server for python',
      author='Simon Pamies',
      author_email='spamsch@gmail.com',
      maintainer='Simon Pamies',
      maintainer_email='spamsch@gmail.com',
      url='http://code.google.com/p/pywebdav/',
      platforms=['Unix', 'Windows'],
      license='GPL',
      version=VERSION,
      long_description="""
      WebDAV library for python. Consists of a server and the DAV package that provides WebDAV functionality.
      After installation of this package you will have a new script in you $PYTHON/bin directory called
      *davserver*. This serves as the main entry point to the server.

      Example
      ::
        davserver -D /home/files -n

      For more information go to http://code.google.com/p/pywebdav/
      """,
      classifiers = [
          'Development Status :: 5 - Production/Stable',
          'Environment :: Console',
          'Environment :: Web Environment',
          'Intended Audience :: End Users',
          'Intended Audience :: Developers',
          'Intended Audience :: System Administrators',
          'License :: OSI Approved :: GNU General Public License (GPL)',
          'Operating System :: MacOS :: MacOS X',
          'Operating System :: POSIX',
          'Programming Language :: Python',
          'Classifier: Topic :: Software Development :: Libraries'
          ],
      keywords = ['webdav',
                  'server',
                  'dav',
                  'standalone',
                  'library',
                  'gpl',
                  'http',
                  'rfc2518',
                  'rfc 2518'],
      packages=['DAV', 'DAVServer'],
      zip_safe=False,
      entry_points={
          'console_scripts' : ['davserver = DAVServer.server:run']
      }
      )
