# Copyright (c) Twisted Matrix Laboratories.
# See LICENSE for details.

"""
Distutils file for building raiser from their Pyrex source
"""

from distutils.core import setup
from distutils.extension import Extension
from Cython.Distutils import build_ext

setup(name='raiser',
      ext_modules=[
          Extension('raiser', ['raiser.pyx'])],
      cmdclass={'build_ext': build_ext})
