|

:ref:`sphinxrst_py<sphinxrst_py>` > suspend_command

.. _suspend_command:

===============
Suspend Command
===============

.. _suspend_command.syntax:

Syntax
------
``{sphinxrst_suspend}``

``{sphinxrst_resume}``

.. _suspend_command.purpose:

Purpose
-------
It is possible to suspend (resume) the sphinxrst extraction during a section.
One begins (ends) the suspension with a suspend command (resume command)
at the
:ref:`beginning of a line<sphinxrst_py.notation.beginning_of_a_line>`.
Note that this will also suspend all other sphinxrst processing; e.g.,
spell checking.

.. _suspend_command.example:

Example
-------
.. toctree::
   :maxdepth: 1

   suspend_exam


----

sphinxrst input file: ``bin/sphinxrst.py``
