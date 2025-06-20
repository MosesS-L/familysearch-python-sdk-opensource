try:
    # Setuptools or Distribute is required to support running `python setup.py test`
    from setuptools import setup
except ImportError:
    # Distutils supports everything else; just run the test suite manually
    from distutils.core import setup

import familysearch

version = familysearch.__version__

setup(
  name = 'familysearch-python-sdk-opensource',
  packages = ['familysearch'],
  version = version,
  description = 'A Python SDK for FamilySearch.org',
  long_description=open('README.rst').read(),
  author = 'Elder Evans',
  author_email = 'elderamevans@gmail.com',
  url = 'https://github.com/elderamevans/familysearch-python-sdk-opensource',
  download_url = 'https://github.com/elderamevans/familysearch-python-sdk-opensource/releases/tag/v' + version, 
  keywords = ['FamilySearch', 'API', 'SDK', 'REST', 'family history', 'geneaolgy', 'JSON'],
  classifiers = [
    "Development Status :: 5 - Production/Stable",
    "Environment :: Console",
    "Environment :: MacOS X",
    "Environment :: Web Environment",
    "Environment :: Win32 (MS Windows)",
    "Environment :: X11 Applications",
    "License :: OSI Approved :: BSD License",
    "Operating System :: OS Independent",
    "Programming Language :: Python :: 3",
    "Programming Language :: Python :: 3.8",
    "Programming Language :: Python :: 3.9",
    "Programming Language :: Python :: 3.10",
    "Programming Language :: Python :: 3.11",
    "Programming Language :: Python :: 3.12",
    "Topic :: Internet :: WWW/HTTP",
    "Topic :: Sociology :: Genealogy",
    "Topic :: Software Development :: Libraries :: Python Modules"
  ],
)
