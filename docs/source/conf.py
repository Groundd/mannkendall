# Configuration file for the Sphinx documentation builder.
#
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
# import os
# import sys
# sys.path.insert(0, os.path.abspath('.'))

# Get the code version from the version file.
from pathlib import Path

# Where are we located ?
file_absolute_path = Path(__file__).absolute()

# Get the version
version_file = file_absolute_path.parents[2] / 'DESCRIPTION'
with version_file.open() as fid:
    vers = next(line.split(":")[1] for line in fid.readlines() if 'Version ' in line)

# -- Project information -----------------------------------------------------

project = 'mannkendall (R)'
copyright = '2020, MeteoSwiss; 2020, Università degli Studi di Modena e Reggio Emilia.'
author = 'Alessandro Bigi'
version = vers

# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = ['sphinx.ext.napoleon',
              'sphinx.ext.todo',  # To get the TODOs visible
              'sphinx.ext.autosectionlabel',  # So we can link directly to the section header names
              #'sphinx.ext.autodoc',  # To get the automatic documentation of functions
             ]

# Specify the parameters of the autodoc, in order to
#autodoc_default_options = {
    # 'members': 'var1, var2',
#    'member-order': 'bysource',
    # 'special-members': '__init__',
    # 'undoc-members': False,
    # 'exclude-members': '__weakref__'
#    }

# To use this nice feature, but still avoid wreaking havoc with sphinx-apidoc
autosectionlabel_prefix_document = True

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = []

# The name of the Pygments (syntax highlighting) style to use.
pygments_style = 'sphinx'

highlight_language = 'R'

# Deal with the todos
todo_include_todos = True
todo_link_only = False

# Napoleon settings (for the docstrings)
napoleon_google_docstring = True
napoleon_numpy_docstring = True
napoleon_include_init_with_doc = True
napoleon_include_private_with_doc = False
napoleon_include_special_with_doc = False
napoleon_use_admonition_for_examples = False
napoleon_use_admonition_for_notes = False
napoleon_use_admonition_for_references = False
napoleon_use_ivar = False
napoleon_use_param = False
napoleon_use_rtype = False
napoleon_use_keyword = False
napoleon_custom_sections = None

# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = 'sphinx_rtd_theme'

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
#html_static_path = ['_static']
