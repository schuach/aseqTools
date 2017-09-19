try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
    "description": "Tools for aseq transformation",
    "author": "Stefan Schuh",
    "url": "URL to get it at.",
    "download_url": "Where to download it.",
    "author_email": "stefan.schuh@uni-graz.at",
    "version": "0.1",
    "install_requires": ["pytest", "xlsxwriter", "easygui"],
    "packages": ["aseqTools"],
    "scripts": ["bin/aseq2xlsx.py"],
    "name": "aseqTools"
}

setup(**config)
