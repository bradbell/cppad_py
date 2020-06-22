# vim: set expandtab:
# -----------------------------------------------------------------------------
#         cppad_py: A C++ Object Library and Python Interface to Cppad
#          Copyright (C) 2017-20 Bradley M. Bell (bradbell@seanet.com)
#              This program is distributed under the terms of the
#              GNU General Public License version 3.0 or later see
#                    https://www.gnu.org/licenses/gpl-3.0.txt
# ----------------------------------------------------------------------------
"""
{sphinxrst_begin spell_exam}

=============
Spell Example
=============

{sphinxrst_file%%# BEGIN_SRC%# END_SRC%}

{sphinxrst_end spell_exam}
"""
# ----------------------------------------------------------------------------
# BEGIN_SRC
"""
{sphinxrst_begin spell_res}
{sphinxrst_spell
    sphinxrst
    iterable
    \cos
    \rm
    \sin
    no no
}


============
Spell Result
============

Text
----
The words ``iterable`` and ``sphinxrst`` are not the dictionary,
so we have included them in the spelling command for this section.


Math
----
The latex commands for greek letters
are automatically included as correct spelling.
Other latex commands in this section; e.g. ``\cos``, ``\sin``, ``\rm``,
have been included in the spelling command for this section.
An alternative is to add them to the
:ref:`spell_list<sphinxrst_py.command_line_arguments.spell_list>`
for all sections:

.. math::

    z = \cos( \theta ) + {\rm i} \sin( \theta )

Double Words
------------
It is consider an error to have only white space between
two occurrences of the same word; e.g.,
no no would be an error if there
were not two occurrences of :code:`no` next to each other in the
spelling command for this section.

:ref:`spell_exam`

{sphinxrst_end spell_res}
"""
# END_SRC
