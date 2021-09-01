#! /usr/bin/env python
# -*- coding:utf-8 -*-
################################
# __author__ = "Lettle"
#QQ:1071445082
#FileName: setup.py
#Version:1.1.1
################################

from setuptools import setup, find_packages

setup(
    name = "DUI",
    version = "1.1.1",
    keywords = ["pip", "uitool","console"],
    description = "A console UI kit.",
    long_description = "A console UI kit. Just for novice.",
    license = "MIT Licence",

    url = "https://github.com/Python-Lettle/DUI",
    author = "Lettle",
    author_email = "1071445082@qq.com",

    packages = find_packages(),
    include_package_data = True,
    platforms = "any",
    install_requires = []
)
