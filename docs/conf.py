# Configuration file for the Sphinx documentation builder.
#
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.

import os
import sys

sys.path.insert(0, os.path.abspath('../'))

# -- Project information -----------------------------------------------------

project = 'TNLTK'
copyright = 'TNLTK'
author = 'Tarık Kaan Koç'

# The full version, including alpha/beta/rc tags
release = '0.99.5'
version = '2 - Pre-Alpha'


# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.

extensions = [
    'sphinx.ext.duration',
    'sphinx.ext.doctest',
    'sphinx.ext.autodoc',
    'sphinx.ext.viewcode',
    'sphinx.ext.autosectionlabel'
]

suppress_warnings = ['autosectionlabel.*']

intersphinx_mapping = {
    'python': ('https://docs.python.org/3/', None),
    'sphinx': ('https://www.sphinx-doc.org/en/master/', None),
}

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = [
    '_build',
    'Thumbs.db',
    '.DS_Store',
    'source/_templates/ISSUES_TEMPLATE.rst',
    'TODO/*'
]

source_suffix = [".rst", ".md"]


# -- Options for HTML output -------------------------------------------------

html_theme = 'sphinx_rtd_theme'


# Below html_theme_options config depends on the theme. 
html_logo = 'source/_static/tnltk_logo_whitte.png'

html_theme_options = {
    'logo_only': True,
    'display_version': True
}

# -- Options for EPUB output
epub_show_urls = 'footnote'