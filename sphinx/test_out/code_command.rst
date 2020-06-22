|

:ref:`sphinxrst_py<sphinxrst_py>` > code_command

.. _code_command:

============
Code Command
============

.. _code_command.syntax:

Syntax
------
``{sphinxrst_code}``

.. _code_command.purpose:

Purpose
-------
A code block, directly below in the current input file, begins with
a line containing the command above.

.. _code_command.requirements:

Requirements
------------
Each code command ends with
a line containing another code command.
Hence there must be an even number of code commands.
The back quote character \` can't be in the same line as the commands.

.. _code_command.rest_of_line:

Rest of Line
------------
Other characters on the same line as a code command
are not included in the sphinxrst output.
This enables one to begin or end a comment block
without having the comment characters in the sphinxrst output.
The file extension in the name of the current input file is used to
determine the source code language for highlighting the code block.
Code blocks as usually small and

.. _code_command.spell_checking:

Spell Checking
--------------
Spell checking is done for these code blocks,
but not for code blocks included using the
:ref:`file command<file_command>`.

.. _code_command.example:

Example
-------
.. toctree::
   :maxdepth: 1

   code_block_exam


----

sphinxrst input file: ``bin/sphinxrst.py``
