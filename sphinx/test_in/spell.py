# -----------------------------------------------------------------------------
#         cppad_py: A C++ Object Library and Python Interface to Cppad
#          Copyright (C) 2017-22 Bradley M. Bell (bradbell@seanet.com)
#              This program is distributed under the terms of the
#              GNU General Public License version 3.0 or later see
#                    https://www.gnu.org/licenses/gpl-3.0.txt
# ----------------------------------------------------------------------------
"""
{xrst_begin_parent spell_exam}

Spell Example
#############

{xrst_literal
    # BEGIN_SRC
    # END_SRC
}

{xrst_end spell_exam}
"""
# ----------------------------------------------------------------------------
# BEGIN_SRC
"""
{xrst_begin spell_res}
{xrst_spell
    iterable
    no no
}


Spell Result
############

Text
****
The words ``iterable`` and ``xrst`` are not the dictionary,
so we have included them in the spelling command for this section.


Math
****
The latex commands for greek letters
are automatically included as correct spelling.
The ``\rm`` command is included by the
:ref:`spelling<xrst_py@command_line_arguments@spelling>`.
The other latex commands in this section, ``\cos`` and ``\sin``,
have been included in the spelling command for this section.
An alternative would be to add them to the *spelling* file
which applies to all sections:

.. math::

    z = \cos( \theta ) + {\rm i} \sin( \theta )

Double Words
************
It is consider an error to have only white space between
two occurrences of the same word; e.g.,
no no would be an error if there
were not two occurrences of :code:`no` next to each other in the
spelling command for this section.

:ref:`@spell_exam`

{xrst_end spell_res}
"""
# END_SRC
