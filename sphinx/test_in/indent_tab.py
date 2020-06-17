# vim: set expandtab:
# -----------------------------------------------------------------------------
#         cppad_py: A C++ Object Library and Python Interface to Cppad
#          Copyright (C) 2017-20 Bradley M. Bell (bradbell@seanet.com)
#              This program is distributed under the terms of the
#              GNU General Public License version 3.0 or later see
#                    https://www.gnu.org/licenses/gpl-3.0.txt
# ----------------------------------------------------------------------------
# BEGIN_SRC
"""
	{begin_sphinxrst indent_tab_py}

	Indent Using Tabs Example
	=========================
	{code_sphinxrst}"""
	def factorial(n) :
		if n == 1 :
			return 1
		return n * factorial(n-1)
	"""{code_sphinxrst}

	Source
	------
	:ref:`indent_tab_src`

	{end_sphinxrst indent_tab_py}
"""
# END_SRC
# ----------------------------------------------------------------------------
"""
{begin_sphinxrst indent_tab_src}

Indent Using Tabs Source
========================

{file_sphinxrst%%# BEGIN_SRC%# END_SRC%}

Example
-------
:ref:`indent_tab_py`

{end_sphinxrst indent_tab_src}
"""
