#!/usr/bin/python

from setuptools import setup, find_packages

setup(
    name="openrazer",
    version="2.4.0",
    packages=find_packages(exclude=["*.tests", "*.tests.*", "tests.*", "tests"])
)
