#!/usr/bin/python

from setuptools import setup, find_packages

setup(
    name="Project",
    version="1.0",
    description="Example Project",
    author="John Doe",
    author_email="john.doe@example.net",
    url="https://www.example.net/",
    packages=find_packages(),
    scripts=["script"],
)
