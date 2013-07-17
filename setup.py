#!/usr/bin/env python
# -*- coding: utf-8 -*-
 
from setuptools import setup
import pywatprop

setup(
    name='pywatprop',
    version=pywatprop.__version__,
    author='Ahmed ELSAYED',
    author_email='ahmed.elsayed@areva.com',
    packages=['pywatprop'],
    license='LICENSE.txt',
    description='Steam / Water Property Functions',
    long_description=open('README.rst').read()
	)
