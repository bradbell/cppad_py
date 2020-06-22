|

:ref:`sphinxrst_py<sphinxrst_py>` > :ref:`spell_exam<spell_exam>` > spell_res

.. _spell_res:

============
Spell Result
============

.. _spell_res.text:

Text
----
The words ``iterable`` and ``sphinxrst`` are not the dictionary,
so we have included them in the spelling command for this section.

.. _spell_res.math:

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

.. _spell_res.double_words:

Double Words
------------
It is consider an error to have only white space between
two occurrences of the same word; e.g.,
no no would be an error if there
were not two occurrences of :code:`no` next to each other in the
spelling command for this section.

:ref:`spell_exam`

----

sphinxrst input file: ``sphinx/test_in/spell.py``
