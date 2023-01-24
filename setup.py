from setuptools import setup, find_packages
import io
with io.open("DESCRIPTION.md", "r", encoding="utf-8") as file:
    DESCRIPTION = file.read()

#  Development Status -> 2 - Pre-Alpha

    setup(
    name="tnltk",
    version= "0.0.1",
    author='Tarik Kaan Koc',
    description= "TNLTK - Turkish Natural Language Toolkit developed by TNLTK Development Team.",
    author_email="tarikkaan1koc@gmail.com",
    long_description = DESCRIPTION,
    long_description_content_type = "text/markdown",
    license = "Apache Software License v2.0",

    packages = find_packages(include=["tnltk.sentence_splitter","tnltk.normalizer"]),
    project_urls={
        "Source": "https://github.com/tnltk/tnltk",
        "Tracker": "https://github.com/tnltk/tnltk/issues",
        "Documentation": "https://tnltk.readthedocs.io"
    },
)