from setuptools import setup, find_packages
import glob
import os
from pkg import __version__, __name__

with open('requirements.txt') as f:
    required = [x for x in f.read().splitlines() if not x.startswith("#")]


setup(
    name = __name__,
    version = __version__,
    description='Skeleton commandline python project',
    author='YOUR NAME',
    packages = find_packages(),
    install_requires=[
        required,
    ],
    entry_points="""
        [console_scripts]
        {name} = pkg.cli:cli
    """.format(name=__name__),
)
