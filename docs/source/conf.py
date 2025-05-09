# Configuration file for the Sphinx documentation builder.

# -- Project information

project = 'project_KB'
copyright = '2025 KB_project'
author = 'wai.lo'

release = '0.1'
version = '0.1.0'

# -- General configuration

extensions = [
    'sphinx.ext.duration',
    'sphinx.ext.doctest',
    'sphinx.ext.autodoc',
    'sphinx.ext.autosummary',
    'sphinx.ext.intersphinx',
]

intersphinx_mapping = {
    'python': ('https://docs.python.org/3/', None),
    'sphinx': ('https://www.sphinx-doc.org/en/master/', None),
}
intersphinx_disabled_domains = ['std']

templates_path = ['_templates']

# -- Options for HTML output

html_theme = 'sphinx_rtd_theme'
html_search_language = 'en'
html_search_options = {'stemming': False}

# -- Options for EPUB output
epub_show_urls = 'footnote'
