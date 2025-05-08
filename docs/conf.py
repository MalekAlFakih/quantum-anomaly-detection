# -- Project information -----------------------------------------------------
project = 'Quantum Anomaly Detection'
author = 'Malek Al Fakih'
release = '0.1.0'

# -- General configuration ---------------------------------------------------
extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.napoleon',
    'sphinx.ext.viewcode',
]

templates_path = ['_templates']
exclude_patterns = []

# -- HTML output -------------------------------------------------------------
html_theme = 'sphinx_rtd_theme'

html_context = {
    "display_github": True,
    "github_user": "MalekAlFakih",
    "github_repo": "quantum-anomaly-detection",
    "github_version": "main",
    "conf_py_path": "/docs/",  # folder where conf.py is located in the GitHub repo
}
