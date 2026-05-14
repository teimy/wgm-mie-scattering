#!/usr/bin/env python

# Author: William G.K. Martin (wgm2111@cu where cu=columbia.edu)
# copyright (c) 2011
# liscence: BSD style


# future
from __future__ import division, absolute_import, print_function


# Import the numpy version of distutils (which has support for f2py)
import os, sys, subprocess
from setuptools import setup, Extension
from setuptools.command.build_ext import build_ext
from os.path import join


# Global names
# ================================================================

NAME = "miescattering"
VERSION = '0.0.1'
DESCRIPTION = (
    "Lorenz-Mie scattering calculations for airborne particles")
AUTHOR = "William G.K. Martin"
AUTHOR_EMAIL = "wgm2111@columbia.edu"
LICENSE = "GPL2"



# Define the folders to find files in \
abs_path = os.getcwd()
FORTRAN_SOURCE_DIR = abs_path+'/src'                     # fortran source files 
PYTHON_SOURCE_DIR = 'mie_scattering'           # python bindings
TARGET_SO_LIB = join(PYTHON_SOURCE_DIR, 'lib') # .so files

# Define the structure of the compiled package
PACKAGES = [PYTHON_SOURCE_DIR, 
            PYTHON_SOURCE_DIR+'.lib']
PACKAGE_DIR = None


# Begin the f2py stuf for building the package
# ================================================================

# Define the fortran extensions to make
ext_modules = [
    Extension(TARGET_SO_LIB+'.'+'wig', 
              sources = [join(FORTRAN_SOURCE_DIR, 'wig.f95'), 
                         join(FORTRAN_SOURCE_DIR, 'fact.f95')]),
    Extension(TARGET_SO_LIB+'.'+'fact', 
              sources = [join(FORTRAN_SOURCE_DIR, 'fact.f95')]),
    Extension(TARGET_SO_LIB+'.'+'lacis', 
              sources = [join(FORTRAN_SOURCE_DIR, 'lacis.f')]), 
    Extension(TARGET_SO_LIB+'.'+'matr', 
              sources = [join(FORTRAN_SOURCE_DIR, 'matr_.f')]), 
    Extension(TARGET_SO_LIB+'.'+'spher', 
              sources = [join(FORTRAN_SOURCE_DIR, 'spher_.f')])]


class F2pyBuildExt(build_ext):
    def build_extension(self, ext):
        module_name = ext.name.split('.')[-1]
        output_dir = join(self.build_lib, *ext.name.split('.')[:-1])
        os.makedirs(output_dir, exist_ok=True)
        subprocess.check_call(
            [sys.executable, '-m', 'numpy.f2py', '-c', *ext.sources, '-m', module_name],
            cwd=output_dir)

# Run setup when called as a program
# --
if __name__ == "__main__":
    setup(name = NAME,
          version = VERSION,
          description = DESCRIPTION,
          author = AUTHOR,
          author_email = AUTHOR_EMAIL,
          packages=PACKAGES,
          package_dir=PACKAGE_DIR,
          license = LICENSE,
          ext_modules=ext_modules,
          cmdclass={'build_ext': F2pyBuildExt})


