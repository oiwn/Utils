import os
from setuptools import setup, find_packages

setup(
    name = 'Utils',
    description = 'Private Web Utils',
    version = '0.0.1',
    url = 'https://github.com/istinspring/Utils',
    author = 'Istinspring',
    author_email = 'istinspring@gmail.com',

    packages = find_packages(),
    include_package_data = True,

    license = "BSD",
    keywords = "keywords search engine scraping parsing",
    classifiers=[
        'Development Status :: 1 - Alpha',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Utilities'
    ],
)
