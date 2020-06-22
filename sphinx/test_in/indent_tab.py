# vim: set expandtab:
# -----------------------------------------------------------------------------
#         cppad_py: A C++ Object Library and Python Interface to Cppad
#          Copyright (C) 2017-20 Bradley M. Bell (bradbell@seanet.com)
#              This program is distributed under the terms of the
#              GNU General Public License version 3.0 or later see
#                    https://www.gnu.org/licenses/gpl-3.0.txt
# ----------------------------------------------------------------------------
"""
{sphinxrst_begin indent_tab_exam}

=========================
Indent Using Tabs Example
=========================

{sphinxrst_file%%# BEGIN_SRC%# END_SRC%}

{sphinxrst_end indent_tab_exam}
"""
# ----------------------------------------------------------------------------
# BEGIN_SRC
"""
	{sphinxrst_begin indent_tab_res}

	========================
	Indent Using Tabs Result
	========================
	{sphinxrst_code}"""
	def factorial(n) :
		if n == 1 :
			return 1
		return n * factorial(n-1)
	"""{sphinxrst_code}

	:ref:`indent_tab_exam`

	{sphinxrst_end indent_tab_res}
"""
# END_SRC
