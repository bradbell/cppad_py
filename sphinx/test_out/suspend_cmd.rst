!!!!!!!!!!!
suspend_cmd
!!!!!!!!!!!

.. toctree::
   :maxdepth: 1
   :hidden:

   suspend_exam

.. meta::
   :keywords: suspend_cmd, suspend, resume, commands

.. index:: suspend_cmd, suspend, resume, commands

.. _suspend_cmd:

Suspend and Resume Commands
###########################
.. contents::
   :local:

.. meta::
   :keywords: syntax

.. index:: syntax

.. _suspend_cmd.syntax:

Syntax
******
- ``\{xrst_suspend}``
- ``\{xrst_resume}``

.. meta::
   :keywords: purpose

.. index:: purpose

.. _suspend_cmd.purpose:

Purpose
*******
It is possible to suspend (resume) the xrst extraction during a section.
One begins (ends) the suspension with a suspend command (resume command)
at the
:ref:`beginning of a line<xrst_py@notation@beginning_of_a_line>`.
Note that this will also suspend all other xrst processing; e.g.,
spell checking.

.. meta::
   :keywords: example

.. index:: example

.. _suspend_cmd.example:

Example
*******

-  :ref:`@suspend_exam`

----

xrst input file: ``bin/xrst.py``
