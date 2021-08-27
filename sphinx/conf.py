# BEGIN conf.py
#
# The conf.py documentation is in
# http://www.sphinx-doc.org/en/master/config
#
# -- Path setup --------------------------------------------------------------
import sphinx_rtd_theme

# -- Project information -----------------------------------------------------
project   = 'cppad_py'
copyright = '2020'
author    = 'Brad Bell'

# -- General configuration ---------------------------------------------------
extensions = [
    'sphinx.ext.mathjax',
    'sphinx_rtd_theme',
]
exclude_patterns = [
    '_build', 'Thumbs.db', '.DS_Store', 'test_out', 'preamble.rst'
]

# -- Options for HTML output -------------------------------------------------
if True :
    html_theme = 'sphinx_rtd_theme'
    html_theme_options = {
        'navigation_depth' : -1   ,
        'titles_only'      : True ,
    }
else :
    html_theme = 'insipid'
    html_theme_options = {
        'strip_section_numbers' : True,
        'nosidebar'             : True,
        'body_centered'         : True,
        'body_max_width'        : None,
        'breadcrumbs'           : True,
    }
# -- These folders are copied to the documentation's HTML output ------------
# html_static_path = [ '_static' ]

# -- These paths are either relative to html_static_path --------------------
# or fully qualified paths (eg. https://...)
html_css_files = [
    'css/custom.css',
]

# -- Latex commands used by all sections -------------------------------------
latex_elements = {
    'preamble' :
        r'\newcommand{\B}[1]{{\bf #1}} '  + '\n' +
        r'\newcommand{\R}[1]{{\rm #1}} '  + '\n' +
        r'\renewcommand{\thesection}{{\hspace{-1em}}}'        + '\n' +
        r'\renewcommand{\thesubsection}{{\hspace{-1em}}}'     + '\n' +
        r'\renewcommand{\thesubsubsection}{{\hspace{-1em}}}'  + '\n' +
        ''
    ,
}
# END conf.py
