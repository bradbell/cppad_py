# This file was automatically generated by xrst
#
# Project information
project = 'cppad_py'
author = ''
#
# General configuration
extensions = [
   'sphinx.ext.mathjax',
]
root_doc = 'index'
html_theme = "furo"
#
rst_prolog = r'''
.. |space| unicode:: 0xA0
.. |tab| replace:: |space| |space| |space|


.. rst-class:: hidden

   :math:`\newcommand{\B}[1]{ {\bf #1} }`
   :math:`\newcommand{\R}[1]{ {\rm #1} }`
'''
#
# Latex used when sphinx builds tex
latex_elements = {
   'preamble' : r'''
   \newcommand{\B}[1]{ {\bf #1} }
   \newcommand{\R}[1]{ {\rm #1} }
   '''
}