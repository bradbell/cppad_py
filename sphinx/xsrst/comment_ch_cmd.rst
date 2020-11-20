!!!!!!!!!!!!!!
comment_ch_cmd
!!!!!!!!!!!!!!

.. toctree::
   :maxdepth: 1
   :hidden:

   comment_ch_exam

.. meta::
   :keywords: comment_ch_cmd, comment, character, command

.. index:: comment_ch_cmd, comment, character, command

.. _comment_ch_cmd:

Comment Character Command
#########################
.. contents::
   :local:

.. meta::
   :keywords: syntax

.. index:: syntax

.. _comment_ch_cmd.syntax:

Syntax
******
``{xsrst_comment_ch`` *ch* :code:`}`

.. meta::
   :keywords: purpose

.. index:: purpose

.. _comment_ch_cmd.purpose:

Purpose
*******
Some languages have a special character that
indicates the rest of the line is a comment.
If you embed sphinx documentation in this type of comment,
you need to inform xsrst of the special character so it does
not end up in your ``.rst`` output file.

.. meta::
   :keywords: ch

.. index:: ch

.. _comment_ch_cmd.purpose.ch:

ch
--
The value of *ch* must be one non white space character.
There must be at least one white space character
between ``xsrst_comment_ch`` and *ch*.
Leading and trailing white space around *ch* is ignored.
There can be only one occurence of this command within a file,
it's effect lasts for the entire file, and
it must come before the first :ref:`begin_cmd` in the file.

.. meta::
   :keywords: beginning, line

.. index:: beginning, line

.. _comment_ch_cmd.beginning_of_a_line:

Beginning of a Line
*******************
A sequence of characters *text* is at the beginning of a line if there
are only space characters
between the previous new line character and *text*.
In addition, the special character *ch* can be the first character
after the new line and before *text*.

.. meta::
   :keywords: input, stream

.. index:: input, stream

.. _comment_ch_cmd.input_stream:

Input Stream
************
The special character (and one space if present directly after)
is removed from the input stream before any xsrst processing; e.g.,
calculating the amount of
:ref:`xsrst_py.Indentation` for the current section.
For example, if :code:`#` is the special character,
the following input has the heading Factorial
and the ``def`` token indented the same amount:

.. code-block:: py

    # Factorial
    # ---------
    def factorial(n) :
        if n == 1 :
            return 1
        return n * factorial(n-1)

.. meta::
   :keywords: example

.. index:: example

.. _comment_ch_cmd.example:

Example
*******

-  :ref:`comment_ch_exam`

----

xsrst input file: ``bin/xsrst.py``
