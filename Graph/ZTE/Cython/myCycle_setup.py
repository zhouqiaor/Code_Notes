from distutils.core import setup
from distutils.extension import Extension
from Cython.Distutils import build_ext
# python myCycle_setup.py build_ext --inplace
setup(
    cmdclass={'build_ext': build_ext},
    ext_modules=[Extension("myCycle0501", ["myCycle0501.pyx"])]
)