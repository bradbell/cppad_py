!!!!!!!!!
spell_res
!!!!!!!!!

.. meta::
   :keywords: spell_res, spell, result

.. index:: spell_res, spell, result

.. _spell_res:

Spell Result
############
- :ref:`spell_res.text`
- :ref:`spell_res.math`
- :ref:`spell_res.double_words`

.. meta::
   :keywords: text

.. index:: text

.. _spell_res.text:

Text
****
The words ``iterable`` and ``xsrst`` are not the dictionary,
so we have included them in the spelling command for this section.

.. meta::
   :keywords: math

.. index:: math

.. _spell_res.math:

Math
****
The latex commands for greek letters
are automatically included as correct spelling.
Other latex commands in this section; e.g. ``\cos``, ``\sin``, ``\rm``,
have been included in the spelling command for this section.
An alternative would be to add them to the
:ref:`spell_file<xsrst_py.command_line_arguments.spell_file>`
which applies to all sections:

.. math::

    z = \cos( \theta ) + {\rm i} \sin( \theta )

.. meta::
   :keywords: double, words

.. index:: double, words

.. _spell_res.double_words:

Double Words
************
It is consider an error to have only white space between
two occurrences of the same word; e.g.,
no no would be an error if there
were not two occurrences of :code:`no` next to each other in the
spelling command for this section.

:ref:`spell_exam`

----

xsrst input file: ``sphinx/test_in/spell.py``
