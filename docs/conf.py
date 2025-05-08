import os
import sys
sys.path.insert(0, os.path.abspath('..'))

project = 'Quantum Anomaly Detection'
copyright = '2025, Mohamed Malek Al Fakih & Abdellah Bichlifen'
author = 'Mohamed Malek Al Fakih & Abdellah Bichlifen'
release = '0.1.0'

extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.napoleon',
    'sphinx.ext.viewcode',
    'sphinx.ext.githubpages',
]

templates_path = ['_templates']
exclude_patterns = []

# -- HTML output -------------------------------------------------------------

html_theme = 'sphinx_rtd_theme'

html_theme_options = {
    'display_version': True,
    'style_external_links': True,
    'vcs_pageview_mode': '',
    'style_nav_header_background': '#2980B9',  # Optional: customize
    'display_github': True,
    'github_user': 'MalekAlFakih',
    'github_repo': 'quantum-anomaly-detection',
    'github_version': 'main',
    'conf_py_path': '/docs/',
}

html_context = {
    "display_github": True,
    "github_user": "MalekAlFakih",
    "github_repo": "quantum-anomaly-detection",
    "github_version": "main",
    "conf_py_path": "/docs/",
}

html_static_path = ['_static']