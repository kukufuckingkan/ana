# setup.py
from setuptools import setup

setup(
    name="moril",
    version="0.0.2",
    packages=["conda"],
    install_requires=[
        pandas,
        pandasql,
        overloading,
        multipledispatch
    ],
)
