#!/usr/bin/env python

from setuptools import setup, find_packages

with open('README.rst') as readme_file:
    readme = readme_file.read()

with open('HISTORY.rst') as history_file:
    history = history_file.read()

setup_requirements = [
    'pytest-runner',
]


setup(
    name='python-humble-utils',
    version='0.3.0',
    url='https://github.com/webyneter/python-humble-utils',

    description="Python utils for everyday use.",
    long_description=readme + '\n\n' + history,

    author="Nikita P. Shupeyko",
    author_email='webyneter@gmail.com',

    packages=find_packages(include=['python_humble_utils']),
    include_package_data=True,

    test_suite='python_humble_utils.tests',

    setup_requires=setup_requirements,
    zip_safe=False,

    entry_points={
        'console_scripts': [
            'python_humble_utils=python_humble_utils.cli:main'
        ]
    },

    license="MIT",
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
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
    ],
)
