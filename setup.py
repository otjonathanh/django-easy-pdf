#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

version = "0.2.0"

if sys.argv[-1] == "publish":
    os.system("python setup.py sdist bdist_wheel upload")
    print("You probably want to also tag the version now:")
    print("  git tag -a %s -m 'version %s'" % (version, version))
    print("  git push --tags")
    sys.exit()

readme = open("README.rst").read()
history = open("HISTORY.rst").read().replace(".. :changelog:", "")

setup(
    name="ot-django-easy-pdf",
    version=version,
    description="""Django PDF views, the easy way""",
    license="MIT",
    author="Jonathan Hayes",
    author_email="jonathanh@opentext.com",
    url="https://github.com/otjonathanh/django-easy-pdf",
    long_description=readme + "\n\n" + history,
    packages=[
        "easy_pdf",
    ],
    include_package_data=True,
    install_requires=[
        "django>=3.0.14",
        "xhtml2pdf>=0.2.5",
        "reportlab>=3",
        'six>=1.16.0'
    ],
    zip_safe=False,
    keywords="django-easy-pdf",
    classifiers=[
        "Development Status :: 4 - Beta",
        "Environment :: Web Environment",
        "Framework :: Django",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Natural Language :: English",
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.4",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Topic :: Software Development :: Libraries :: Python Modules"
    ],
)
