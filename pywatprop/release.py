# -*- coding: utf-8 -*-
"""Release data for the pyfortreader project."""

#-----------------------------------------------------------------------------
#  Copyright (c) 2013, AREVA - <todd.matthews@areva.com>
#
#  Not Distributed at this time.
#
#  A full license may be added in the file COPYING.txt, distributed with this software.
#-----------------------------------------------------------------------------

# Name of the package for release purposes.  This is the name which labels
# the tarballs and RPMs made by distutils, so it's best to lowercase it.
name = 'pywatprop'

# TranBase version information.  An empty _version_extra corresponds to a full
# release.  'dev' as a _version_extra string means this is a development
# version
_version_major = 0
_version_minor = 1
_version_micro = ''  # use '' for first of series, number for 1 and above
_version_extra = 'dev'
#_version_extra = 'rc1'
#_version_extra = ''  # Uncomment this for full releases

# Construct full version string from these.
_ver = [_version_major, _version_minor]
if _version_micro:
    _ver.append(_version_micro)
if _version_extra:
    _ver.append(_version_extra)

__version__ = '.'.join(map(str, _ver))

version = __version__  # backwards compatibility name

description = "pywatprop: Lookup functions for water / steam properties"

long_description = \
"""
pywatprop provides a set of water property routines based on the
freesteam package. It adds the ability to pass vectors as parameters.
"""

license = 'None'

authors = {'Todd' : ('M. Todd Matthews','todd.matthews@areva.com'),
            'Ahmed': ('Ahmed Elsayed', 'ahmed.elsayed@areva.com')
          }

author = 'The TranBase Development Team'

author_email = 'todd.matthews@areva.com'

url = 'http://www.tranbase.org'

# This will only be valid for actual releases sent to PyPI, but that's OK since
# those are the ones we want pip/easy_install to be able to find.
# KEPT FOR USE LATER - NOT VALID INFORMATION AT THIS TIME
download_url = 'http://archive.tranbase.org/release/%s' % version

platforms = ['Linux']

keywords = ['Transients']

classifiers = [
    'Intended Audience :: Engineers',
    'License :: None',
    'Programming Language :: Python',
    'Programming Language :: Python :: 2',
    'Programming Language :: Python :: 2.7',
    'Topic :: System :: Computing',
    ]

