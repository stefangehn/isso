#!/usr/bin/env python3
# -*- encoding: utf-8 -*-

import os
import setuptools.command.build_py
import subprocess
import sys

from setuptools import setup, find_packages

requires = ['itsdangerous', 'Jinja2', 'misaka>=2.0,<3.0', 'html5lib',
            'werkzeug>=1.0', 'bleach', 'flask-caching>=1.9']

if sys.version_info < (3, ):
    raise SystemExit("Python 2 is not supported.")
elif (3, 0) <= sys.version_info < (3, 5):
    raise SystemExit("Python 3 versions < 3.5 are not supported.")


class NpmBuildCommand(setuptools.command.build_py.build_py):
    """Prefix Python build with node-based asset build"""

    def run(self):
        if 'TOX_ENV' not in os.environ:
            subprocess.check_call(['make', 'init', 'js'])
        setuptools.command.build_py.build_py.run(self)


setup(
    name='isso',
    version='0.12.5',
    author='Martin Zimmermann',
    author_email='info@posativ.org',
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    url='https://github.com/posativ/isso/',
    license='MIT',
    description='lightweight Disqus alternative',
    classifiers=[
        "Development Status :: 4 - Beta",
        "Topic :: Internet",
        "Topic :: Internet :: WWW/HTTP :: HTTP Servers",
        "Topic :: Internet :: WWW/HTTP :: WSGI :: Application",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8"
    ],
    install_requires=requires,
    setup_requires=["cffi>=1.3.0"],
    entry_points={
        'console_scripts':
            ['isso = isso:main'],
    },
    cmdclass={
        'build_py': NpmBuildCommand,
    },
)
