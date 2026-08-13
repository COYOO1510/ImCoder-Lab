# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'ImCoder Lab'
copyright = '2026, COYOO'
author = 'COYOO'
release = 'V1.0'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = ['myst_parser', 'sphinx_rtd_theme']

templates_path = ['_templates']
exclude_patterns = []

language = 'zh_CN'

# 支持 markdown 文件
source_suffix = {
    '.rst': 'restructuredtext',
    '.md': 'markdown',
}

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'sphinx_rtd_theme'
html_static_path = ['_static']

# 网站 Logo（显示在侧边栏顶部）
html_logo = '_static/images/logo.svg'

# 加载自定义 CSS
html_css_files = [
    'custom.css',
]