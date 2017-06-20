#!/usr/bin/env python

import os
from typing import Sequence

from setuptools import setup, find_packages

with open('README.rst') as readme_file:
    readme = readme_file.read()

with open('HISTORY.rst') as history_file:
    history = history_file.read()


# region requirements
# Source: https://github.com/celery/celery/blob/master/setup.py

def parse_requirements(*paths: str) -> Sequence[str]:
    return [req for subreq in _requirements(*paths) for req in subreq]


def _requirements(*paths: str) -> list:
    return [
        _pip_requirement(r)
        for r in
        (
            _strip_comment(l)
            for l in
            open(os.path.join(os.getcwd(), 'requirements', *paths)).readlines()
        )
        if r
    ]


def _pip_requirement(requirement: str) -> Sequence[str]:
    if requirement.startswith('-r '):
        _, path = requirement.split()
        return parse_requirements(*path.split('/'))
    return [requirement]


def _strip_comment(s):
    return s.split('#', 1)[0].strip()


install_requirements = [
    'Click>=6.0',
]

setup_requirements = [
    'pytest-runner',
]

# endregion


setup(
    name='python_humble_utils',
    version='0.1.0',
    url='https://github.com/webyneter/python_humble_utils',

    description="Python utils for everyday use.",
    long_description=readme + '\n\n' + history,

    author="Nikita P. Shupeyko",
    author_email='webyneter@gmail.com',

    packages=find_packages(include=['python_humble_utils']),
    include_package_data=True,
    install_requires=install_requirements,

    test_suite='python_humble_utils.tests',
    tests_require=parse_requirements('test.txt'),

    entry_points={
        'console_scripts': [
            'python_humble_utils=python_humble_utils.cli:main'
        ]
    },

    setup_requires=setup_requirements,
    zip_safe=False,

    license="MIT license",
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Programming Language :: Python :: ',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
    ],
    keywords=[
        'python',
        'humble',
        'utility',
        'utilities',
        'util',
        'utils',
        'helper',
        'helpers',
        'command',
        'commands',
    ],
)
