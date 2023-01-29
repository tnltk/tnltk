import io
import os
import re

import setuptools


def get_long_description():
    base_dir = os.path.abspath(os.path.dirname(__file__))
    with io.open(os.path.join(base_dir, "README.rst"), encoding="utf-8") as f:
        return f.read()


def get_version():
    current_dir = os.path.abspath(os.path.dirname(__file__))
    version_file = os.path.join(current_dir, "tnltk", "__init__.py")
    with io.open(version_file, encoding="utf-8") as f:
        return re.search(r'^__version__ = [\'"]([^\'"]*)[\'"]', f.read(), re.M).group(1)


setuptools.setup(
    name="tnltk",
    version=get_version(),
    author="Tarik Kaan Koc",
    email="tarikkaan1koc@gmail.com",
    license="Apache License, Version 2.0",
    description="TNLTK - Turkish Natural Language Toolkit developed by TNLTK Development Team.",
    long_description=get_long_description(),
    long_description_content_type="text/markdown",
    url="https://github.com/tnltk/tnltk",
    Tracker="https://github.com/tnltk/tnltk/issues",
    Documentation="https://tnltk.readthedocs.io",
    packages=setuptools.find_packages(exclude=["tests"]),
    python_requires=">=3.7",
    classifiers=[
        "Development Status :: 2 - Pre-Alpha",
        "Intended Audience :: Developers",
        "Intended Audience :: Education",
        "Intended Audience :: Science/Research",
        "Topic :: Scientific/Engineering",
        "Topic :: Scientific/Engineering :: Artificial Intelligence",
        "Topic :: Scientific/Engineering :: Information Analysis",
        "Topic :: Text Processing",
        "Topic :: Software Development",
        "Topic :: Software Development :: Libraries",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
    ],
    keywords="machine-learning, deep-learning, ml, nlp, turkish-nlp",
)
