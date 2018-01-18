from distutils.core import setup
from distutils.extension import Extension
from Cython.Build import cythonize
from os.path import join
from os import getcwd
import glob
import numpy

pwd = getcwd()

sources = [join(pwd, 'pcg.pyx')] + ['pcg-advance-32.c', 'pcg-advance-64.c','pcg-output-32.c','pcg-rngs-32.c']

setup(
    ext_modules = cythonize([Extension("pcg",
                             sources=sources,
                             include_dirs=[pwd,numpy.get_include()],

                             extra_compile_args=['-std=c99'])])
)
