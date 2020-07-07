|

:ref:`xsrst_py<xsrst_py>` > :ref:`comment_ch_cmd<comment_ch_cmd>` > :ref:`comment_ch_exam<comment_ch_exam>` > comment_ch_res

.. meta::
   :keywords: comment_ch_res, begin, special, character, result

.. index:: comment_ch_res, begin, special, character, result

.. _comment_ch_res:

==============================
Begin Special Character Result
==============================
In the original source, the leading characters '#' and ' ' get removed
and the remaining text lines up with the ``def`` below:

.. code-block:: py

    def factorial(n) :
        if n == 1 :
            return 1
        return n * factorial(n-1)

:ref:`comment_ch_exam`

----

xsrst input file: ``sphinx/test_in/comment_ch.py``
