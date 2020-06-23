|

:ref:`xsrst_py<xsrst_py>` > spell_cmd

.. meta::
   :keywords: spell, command

.. index:: spell, command

.. _spell_cmd:

=============
Spell Command
=============

.. meta::
   :keywords: syntax

.. index:: syntax

.. _spell_cmd.syntax:

Syntax
------
``{xsrst_spell`` *word_1* ...  *word_n*:code:`}`

Here *word_1*, ..., *word_n* is the special list of words for this section.
In the syntax above the list of words is all in one line,
but they could be on different lines.
Each word starts with an upper case letter,
a lower case letter, or a back slash.
The back slash is included as a possible beginning of a word
so that latex commands can be included in the spelling list.
The rest of the characters in a word are lower case letters.

.. meta::
   :keywords: purpose

.. index:: purpose

.. _spell_cmd.purpose:

Purpose
-------
You can specify a special list of words
(not normally considered correct spelling)
for the current section using the command above at the
:ref:`beginning of a line<xsrst_py.notation.beginning_of_a_line>`.

.. meta::
   :keywords: spell_file

.. index:: spell_file

.. _spell_cmd.spell_file:

spell_file
----------
The list of words in
:ref:`spell_file<xsrst_py.command_line_arguments.spell_file>`
are considered correct spellings for all sections.
The latex commands corresponding to the letters in the greek alphabet
are automatically added to this list.

.. meta::
   :keywords: capitalized, words

.. index:: capitalized, words

.. _spell_cmd.capitalized_words:

Capitalized Words
-----------------
The case of the first letter does not matter when checking spelling;
e.g., if ``abcd`` is *word_1* then ``Abcd`` will be considered a valid word.

.. meta::
   :keywords: double, words

.. index:: double, words

.. _spell_cmd.double_words:

Double Words
------------
It is considered an error to have only white space between two occurrences
of the same word.

.. meta::
   :keywords: example

.. index:: example

.. _spell_cmd.example:

Example
-------
.. toctree::
   :maxdepth: 1

   spell_exam


----

xsrst input file: ``bin/xsrst.py``