.. _get_cppad_mixed_sh-name:

!!!!!!!!!!!!!!!!!!
get_cppad_mixed_sh
!!!!!!!!!!!!!!!!!!

.. raw:: html

   <a href="_sources/get_cppad_mixed_sh.rst.txt">View page source</a>

.. meta::
   :keywords: get_cppad_mixed_sh, get, cppad_mixed

.. index:: get_cppad_mixed_sh, get, cppad_mixed

.. _get_cppad_mixed_sh-title:

Get cppad_mixed
###############

.. meta::
   :keywords: syntax

.. index:: syntax

.. _get_cppad_mixed_sh@Syntax:

Syntax
******
``bin/get_cppad_mixed.sh``

.. meta::
   :keywords: top, source, directory

.. index:: top, source, directory

.. _get_cppad_mixed_sh@Top Source Directory:

Top Source Directory
********************
This program must be run from the
:ref:`top_source_directory<setup_py@Download@Top Source Directory>`.

.. meta::
   :keywords: purpose

.. index:: purpose

.. _get_cppad_mixed_sh@Purpose:

Purpose
*******
If you are going to use the python ``cppad_mixed`` module,
you will need to run this script to install the corresponding
C++ module. This script includes the installation of cppad so it is not
necessary to also run :ref:`get_cppad_sh-name`.

.. meta::
   :keywords: settings

.. index:: settings

.. _get_cppad_mixed_sh@Settings:

Settings
********
This scripts uses the
:ref:`get_cppad_sh settings<get_cppad_sh@Settings>` for
*cmake_install_prefix* , *extra_cxx_flags*, and *build_type* .
