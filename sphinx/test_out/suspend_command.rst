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

|

``{sphinxrst_resume}``

.. _suspend_command.purpose:

Purpose
-------
It is possible to suspend the sphinxrst extraction during a section.
One begins the suspension with a suspend command at the
:ref:`beginning of a line<sphinxrst_py.notation.beginning_of_a_line>`.
Note that this will also suspend all other sphinxrst processing; e.g.,
spell checking.

.. _suspend_command.resume_command:

Resume Command
--------------
One resumes the extraction with a resume command at the beginning of a line.
Each suspend command must have a corresponding resume command in same
section (between the corresponding begin sphinxrst and end sphinxrst commands).

.. _suspend_command.example:

Example
-------
.. toctree::
   :maxdepth: 1

   suspend_exam


----

sphinxrst input file: ``bin/sphinxrst.py``
