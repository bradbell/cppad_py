|

:ref:`xsrst_py<xsrst_py>` > suspend_cmd

.. meta::
   :keywords: suspend_cmd, suspend, and, resume, command

.. index:: suspend_cmd, suspend, and, resume, command

.. _suspend_cmd:

==========================
Suspend and Resume Command
==========================

.. meta::
   :keywords: syntax

.. index:: syntax

.. _suspend_cmd.syntax:

Syntax
------
- ``{xsrst_suspend}``
- ``{xsrst_resume}``

.. meta::
   :keywords: purpose

.. index:: purpose

.. _suspend_cmd.purpose:

Purpose
-------
It is possible to suspend (resume) the xsrst extraction during a section.
One begins (ends) the suspension with a suspend command (resume command)
at the
:ref:`beginning of a line<xsrst_py.notation.beginning_of_a_line>`.
Note that this will also suspend all other xsrst processing; e.g.,
spell checking.

.. meta::
   :keywords: example

.. index:: example

.. _suspend_cmd.example:

Example
-------
.. toctree::
   :maxdepth: 1

   suspend_exam


----

xsrst input file: ``bin/xsrst.py``
