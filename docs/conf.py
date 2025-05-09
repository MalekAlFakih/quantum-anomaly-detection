project = 'Quantum Anomaly Detection'
copyright = '2025'
author = 'Mohamed Malek Al Fakih & Abdellah Bichlifen'
release = '0.2.1'

extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.mathjax',
    'sphinx.ext.napoleon',
    'sphinx.ext.viewcode'
]

templates_path = ['_templates']
exclude_patterns = []
html_theme = 'sphinx_rtd_theme'
html_static_path = ['_static']

html_context = {
    "display_github": True,
    "github_user": "MalekAlFakih",
    "github_repo": "quantum-anomaly-detection",
    "github_version": "main",
    "conf_py_path": "/docs/",
}
