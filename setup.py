#!/usr/bin/env python
# -*- coding: utf-8 -*-

from pathlib import Path
from setuptools import setup, find_packages

setup(
    author="Adam Dyess",
    author_email="adam.dyess@canonical.com",
    description="Silly package to demonstrate unit testing",
    long_description=Path("README.md").read_text(),
    long_description_content_type='text/markdown',
    classifiers=[
        "Framework :: Pytest",
        "Programming Language :: Python",
        "Topic :: Software Development :: Testing",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
    ],
    license="MIT license",
    include_package_data=True,
    keywords=["pytest", "yaml", "asyncio"],
    name="testing-for-fun",
    packages=find_packages(include=["testing_for_fun"]),
    url="https://github.com/addyess/testing_for_fun",
    version="0.0.1",
    zip_safe=True,
    install_requires=["aiohttp", "lxml" ],
    entry_points=dict(
        console_scripts=[
            'testing_for_fun = testing_for_fun:main'
        ]
    )
)
