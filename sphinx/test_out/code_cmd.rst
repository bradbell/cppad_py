.. meta::
   :keywords: code_cmd, code, command

.. index:: code_cmd, code, command

.. _code_cmd:

Code Command
############

.. meta::
   :keywords: syntax

.. index:: syntax

.. _code_cmd.syntax:

Syntax
******
- ``{xsrst_code`` *language* :code:`}`
- ``{xsrst_code}``

.. meta::
   :keywords: purpose

.. index:: purpose

.. _code_cmd.purpose:

Purpose
*******
A code block, directly below in the current input file, begins with
a line containing the first version ( *language* included version)
of the command above.

.. meta::
   :keywords: requirements

.. index:: requirements

.. _code_cmd.requirements:

Requirements
************
Each code command ends with
a line containing the second version of the command; i.e., ``{xsrst_code}``.
Hence there must be an even number of code commands.
The back quote character \` can't be in the same line as the commands.

.. meta::
   :keywords: language

.. index:: language

.. _code_cmd.language:

language
********
A *language* is a non-empty sequence of non-space the characters.
It is used to determine the source code language
for highlighting the code block.

.. meta::
   :keywords: rest, of, line

.. index:: rest, of, line

.. _code_cmd.rest_of_line:

Rest of Line
************
Other characters on the same line as a code command
are not included in the xsrst output.
This enables one to begin or end a comment block
without having the comment characters in the xsrst output.

.. meta::
   :keywords: spell, checking

.. index:: spell, checking

.. _code_cmd.spell_checking:

Spell Checking
**************
Code blocks as usually small and
spell checking is done for these code blocks.
(Spell checking is not done for code blocks included using the
:ref:`file command<file_cmd>` .)

.. meta::
   :keywords: example

.. index:: example

.. _code_cmd.example:

Example
*******
.. toctree::
   :maxdepth: 1

   code_exam


----

xsrst input file: ``bin/xsrst.py``
