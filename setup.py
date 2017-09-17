try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
    "description": "My Project",
    "author": "Stefan Schuh",
    "url": "URL to get it at.",
    "download_url": "Where to download it.",
    "author_email": "stefan.schuh@uni-graz.at",
    "version": "0.1",
    "install_requires": ["nose"],
    "packages": ["NAME"],
    "scripts": [],
    "name": "projectname"
}

setup(**config)
https://docs.python.org/3/library/tkinter.html#module-tkinter
