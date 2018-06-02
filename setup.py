#!/usr/bin/env python

from setuptools import setup, find_packages
import os

def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

# Full list of classifiers can be found here:
# https://pypi.org/pypi?%3Aaction=list_classifiers
CLS = (
  'Development Status :: 3 - Alpha',
  'License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)',
  'Environment :: Web Environment',
  'Framework :: Flask',
  'Intended Audience :: Developers',
  'Operating System :: OS Independent',
  'Programming Language :: Python',
  'Topic :: Internet :: WWW/HTTP :: WSGI :: Application',
)
REQS = (
    'flask >= 1.0.0',
    'click >= 6.7',
    'jinja2 >= 2.10',
    'markupSafe >= 1.0',
    'werkzeug >= 0.14.1',
    'six >= 1.11.0',
)
TEST_REQS = (
    'pytest >= 3.6.0',
    'tox >= 3.0.0',
)
SRC = 'src'
TESTS = ('*.tests', 'tests.*', '*.tests.*', 'tests')
PKG_DATA = {
    'apptester': ['*.md'],
}

setup(
    name='apptester',
    description='App to test app-server configuration',
    version='0.1',
    author='Michal Grochmal',
    author_email='NmiOkeS@PgroAchmalM.org',
    license='GNU General Public License, version 3 or later',
    url='https://github.com/grochmal/apptester',
    long_description=read('README'),
    packages=find_packages(SRC, exclude=TESTS),
    package_dir={'': SRC},
    include_package_data=True,
    package_data=PKG_DATA,
    classifiers=CLS,
    install_requires=REQS,
    tests_require=TEST_REQS,
    extras_require={'test': TEST_REQS}
)

