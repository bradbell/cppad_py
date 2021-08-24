# -----------------------------------------------------------------------------
#         cppad_py: A C++ Object Library and Python Interface to Cppad
#          Copyright (C) 2017-21 Bradley M. Bell (bradbell@seanet.com)
#              This program is distributed under the terms of the
#              GNU General Public License version 3.0 or later see
#                    https://www.gnu.org/licenses/gpl-3.0.txt
# ----------------------------------------------------------------------------
"""
{xsrst_begin_parent heading_exam}

Heading Example
###############

{xsrst_file
    # BEGIN_SRC
    # END_SRC
}

Child Sections
**************
The heading above (Child Sections) is an example heading for the
:ref:`children<xsrst_py.links_to_headings.children>`
of a
:ref:`parent section<xsrst_py.table_of_contents.parent_section>`.

{xsrst_end heading_exam}
"""
# ----------------------------------------------------------------------------
# BEGIN_SRC
"""
{xsrst_begin heading_res}

Heading Result
##############
The label for this heading is the section name ``heading_res``.

Second Level
************
The label for this heading is ``heading_res.second_level``.

Third Level
===========
The label for this heading is ``heading_res.second_level.third_level``.

Another Second Level
********************
The label for this heading is ``heading_res.another_second_level``.

Third Level
===========
The label for this heading is
``heading_res.another_second_level.third_level``.

Links
*****
These links would also work from any other section because the
:ref:`section_name<begin_cmd.section_name>`
(which is ``heading_res`` in this case)
is included at the beginning of the target for the link:

1. :ref:`heading_res`
2. :ref:`heading_res.second_level`
3. :ref:`heading_res.second_level.third_level`
4. :ref:`heading_res.another_second_level`
5. :ref:`heading_res.another_second_level.third_level`

:ref:`heading_exam`

{xsrst_end heading_res}
"""
# END_SRC
