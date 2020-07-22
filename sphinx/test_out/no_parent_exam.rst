.. meta::
   :keywords: no_parent_exam, no, parent, example

.. index:: no_parent_exam, no, parent, example

.. _no_parent_exam:

No Parent Example
#################

All the sections in the file ``children.py``
are children of the section below
because ``children.py`` does not have a
:ref:`parent section<begin_cmd.parent_section>`:

.. literalinclude:: ../../sphinx/test_in/no_parent.xsrst
    :lines: 25-48

.. toctree::
   :maxdepth: 1

   no_parent_res

----

xsrst input file: ``sphinx/test_in/no_parent.xsrst``
