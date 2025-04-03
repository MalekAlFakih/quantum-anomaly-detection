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
'sphinx.ext.viewcode'
]

templates_path = ['_templates']
exclude_patterns = []

html_theme = 'alabaster'
html_static_path = ['_static']
