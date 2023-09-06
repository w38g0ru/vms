# conf.py
import sphinx_rtd_theme

project = 'Vacancy Management System Documentation'
author = 'Anish Bhattarai'
master_doc = 'index'
extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.napoleon',
    'sphinx_rtd_theme',
]
html_theme = 'sphinx_rtd_theme'
html_theme_path = [sphinx_rtd_theme.get_html_theme_path()]
