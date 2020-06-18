.. _spell_py:

=============
Spell Example
=============

.. _spell_py.text:

Text
----
The words ``iterable`` and ``sphinxrst`` are not the dictionary,
so we have included them in the spelling command for this section.

.. _spell_py.math:

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

.. _spell_py.double_words:

Double Words
------------
It is consider an error to have only white space between
two occurrences of the same word; e.g.,
no no would be an error if there
were not two occurrences of :code:`no` next to each other in the
spelling command for this section.

.. _spell_py.source:

Source
------
:ref:`spell_src`

----

sphinxrst_input_file: ``sphinx/test_in/spell.py``
