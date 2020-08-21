#!/usr/bin/env python

from distutils.core import setup

setup(
    name='python-yay',
    version='0.4.2',
    description='Simple Python interface to Arch Linux package manager (yay)',
    author='Matt Spurrier',
    author_email='matthew@spurrier.com.au',
    url='https://github.com/digitalsparky/python-yay',
    py_modules=['yay'],
    keywords = ['yay', 'arch linux'],
    download_url = 'https://github.com/digitalsparky/python-yay/archive/0.4.2.tar.gz',
    license = 'GPLv3',
    classifiers = [
    	"Development Status :: 3 - Alpha",
    	"License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)",
    	"Operating System :: Unix",
    	"Topic :: System :: Software Distribution",
    ]
)
