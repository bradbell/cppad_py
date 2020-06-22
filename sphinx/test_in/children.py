# vim: set expandtab:
# -----------------------------------------------------------------------------
#         cppad_py: A C++ Object Library and Python Interface to Cppad
#          Copyright (C) 2017-20 Bradley M. Bell (bradbell@seanet.com)
#              This program is distributed under the terms of the
#              GNU General Public License version 3.0 or later see
#                    https://www.gnu.org/licenses/gpl-3.0.txt
# ----------------------------------------------------------------------------
"""
{sphinxrst_begin children_exam}

===========================
Indent and Children Example
===========================

{sphinxrst_file%%# BEGIN_SRC%# END_SRC%}

{sphinxrst_end children_exam}
"""
# ----------------------------------------------------------------------------
# BEGIN_SRC
"""
{sphinxrst_begin children_res}

==========================
Indent and Children Result
==========================

Children
--------
This example has a children command and the corresponding links are
automatically placed directly below; i.e., where the command is located.

{sphinxrst_children%
    %sphinx/test_in/indent_space.py
    %sphinx/test_in/indent_tab.py
%}

Example
-------
:ref:`children_exam`

{sphinxrst_end children_res}
"""
# END_SRC
