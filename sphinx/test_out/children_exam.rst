!!!!!!!!!!!!!
children_exam
!!!!!!!!!!!!!

.. meta::
   :keywords: children_exam, children, example

.. index:: children_exam, children, example

.. _children_exam:

Children Example
################
- :ref:`children_exam.other_section`
- :ref:`children_exam.this_file`

This file does not contain a begin parent command,
so all its sections are children of the section that includes it.

.. meta::
   :keywords: other, section

.. index:: other, section

.. _children_exam.other_section:

Other Section
*************
The :ref:`link<children_other>` goes to the other section in this file.

.. meta::
   :keywords: this, file

.. index:: this, file

.. _children_exam.this_file:

This File
*********

.. literalinclude:: ../../../sphinx/test_in/children.py
    :lines: 9-41
    :language: py

----

xsrst input file: ``sphinx/test_in/children.py``
