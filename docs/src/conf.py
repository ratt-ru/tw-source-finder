# Configuration file for the Sphinx documentation builder.
#
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html


# WORKAROUND: https://github.com/sphinx-doc/sphinx/issues/9243
import sphinx.builders.html
import sphinx.builders.latex
import sphinx.builders.texinfo
import sphinx.builders.text
import sphinx.ext.autodoc

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
import os
import sys
sys.path.insert(0, os.path.abspath("../../src"))


# -- Project information -----------------------------------------------------

project = 'tw-source-finder'
copyright = '2022, Tony Willis'
author = 'Tony Willis'

# The full version, including alpha/beta/rc tags
release = '0.0.1'


# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    "sphinx.ext.autodoc",
    "sphinx.ext.doctest",
    "sphinx.ext.intersphinx",
    "sphinx.ext.mathjax",
    "sphinx.ext.todo",
    "sphinx.ext.viewcode",
    "sphinx_autodoc_typehints",
]

autodoc_mock_imports = [
    "numpy",
    "astropy",
    "scipy",
    "shapely",
    "skimage",
    "matplotlib",
    "pycurl",
    "reproject",
    "pyheal",
]

autodoc_default_options = {
    "members": True,
    "special-members": "__init__",
}

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = []


# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = 'sphinx_rtd_theme'

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']

# left-align all math blocks in Sphinx 
mathjax3_config = {'chtml': {'displayAlign': 'left'}}
