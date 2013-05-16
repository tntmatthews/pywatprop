# encoding: utf-8
"""
pywatprop: lookup functions for water properties

http://www.areva.com
"""
#-----------------------------------------------------------------------------
#  Copyright (c) 2013, AREVA
#
#  Not Distributed at this time.
#
#  Later a full license may be added in the file COPYING.txt,
#  distributed with this software.
#-----------------------------------------------------------------------------

#-----------------------------------------------------------------------------
# Imports
#-----------------------------------------------------------------------------
import os
import sys

#-----------------------------------------------------------------------------
# Setup everything
#-----------------------------------------------------------------------------

# Don't forget to also update setup.py when this changes!
if sys.version_info[:2] < (2, 7):
    raise ImportError('Python Version 2.7 or above is required for pywatprop.')


# Release data
import release
__author__ = ''
for author, email in release.authors.itervalues():
    __author__ += author + ' <' + email + '>\n'
__license__  = release.license
__version__  = release.version

from watprop import watprop
from steamtab import steamtab