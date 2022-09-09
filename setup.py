from os import path

from setuptools import setup

# version
VERSION = '0.1.15'

# requirements
REQUIRED_PYTHON = '>=3.8.0'
REQUIRED_PACKAGES = ['pandas', 'pyperclip']

# Package meta-data
NAME = 'cvhero'
DESCRIPTION = 'copy paste pandas'
SOURCE_URL = 'https://github.com/stryder-git/cvhero'
AUTHOR = 'Marcel Pieper'
EMAIL = 'marcel.pieper@outlook.com'
LICENSE = 'MIT'

# ----- items below do not generally change ------- #

# Get the long description from the README file
here = path.abspath(path.dirname(__file__))
with open(path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    # meta data
    name=NAME,
    version=VERSION,
    description=DESCRIPTION,
    long_description=long_description,
    long_description_content_type='text/markdown',
    url=SOURCE_URL,
    author=AUTHOR,
    author_email=EMAIL,
    license=LICENSE,
    project_urls={
        'Source': SOURCE_URL,
    },

    # See https://pypi.python.org/pypi?%3Aaction=list_classifiers
    classifiers=[
        # How mature is this project? Common values are
        #   4 - Beta
        #   5 - Production/Stable
        'Development Status :: 4 - Beta',

        # Indicate who your project is intended for
        'Intended Audience :: Developers',
        'Topic :: Software Development',

        # Pick your license as you wish (should match "license" above)
        'License :: OSI Approved :: MIT License',

        # Specify the Python versions you support here.
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
    ],

    # What does your project relate to?
    keywords='pandas testing copy paste',

    # requirements
    packages=["cvhero"],
    python_requires=REQUIRED_PYTHON,
    install_requires=REQUIRED_PACKAGES,
    tests_require=['pytest'],
)