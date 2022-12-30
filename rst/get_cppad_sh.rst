.. _get_cppad_sh-name:

!!!!!!!!!!!!
get_cppad_sh
!!!!!!!!!!!!

.. raw:: html

   <a href="_sources/get_cppad_sh.rst.txt">View page source</a>

.. meta::
   :keywords: get_cppad_sh, get, cppad

.. index:: get_cppad_sh, get, cppad

.. _get_cppad_sh-title:

Get Cppad
#########

.. meta::
   :keywords: syntax

.. index:: syntax

.. _get_cppad_sh@Syntax:

Syntax
******
``bin/get_cppad.sh``

.. meta::
   :keywords: top, source, directory

.. index:: top, source, directory

.. _get_cppad_sh@Top Source Directory:

Top Source Directory
********************
This program must be run from the
:ref:`top_source_directory<setup_py@Download@Top Source Directory>`.

.. meta::
   :keywords: settings

.. index:: settings

.. _get_cppad_sh@Settings:

Settings
********
If you change any of these settings, you must re-run ``get_cppad.sh`` .

.. meta::
   :keywords: cmake_install_prefix

.. index:: cmake_install_prefix

.. _get_cppad_sh@Settings@cmake_install_prefix:

cmake_install_prefix
====================
This prefix is used to install cppad_py. It may be a local directory; e.g.,
``build/prefix`` or an absolute path; e.g., ``/usr/local``.
It may include the shell variable ``$HOME`` but no other variables:

.. literalinclude:: ../bin/get_cppad.sh
   :lines: 42-42
   :language: sh

If this prefix does no start with ``/``, it is relative to the
:ref:`top_source_directory<setup_py@Download@Top Source Directory>`.
Note that ``$HOME`` starts with ``/``.

.. meta::
   :keywords: extra_cxx_flags

.. index:: extra_cxx_flags

.. _get_cppad_sh@Settings@extra_cxx_flags:

extra_cxx_flags
===============
Extra compiler flags used when compiling c++ code not including the
debugging and optimization flags.
The ones below are example flags are used by g++:

.. literalinclude:: ../bin/get_cppad.sh
   :lines: 54-54
   :language: sh

.. meta::
   :keywords: build_type

.. index:: build_type

.. _get_cppad_sh@Settings@build_type:

build_type
==========
This must be must ``debug`` or ``release`` .
The debug version has more error messaging while the release
version runs faster.

.. literalinclude:: ../bin/get_cppad.sh
   :lines: 63-63
   :language: sh

.. meta::
   :keywords: cmake_install_prefix

.. index:: cmake_install_prefix

.. _get_cppad_sh@Settings@build_type@cmake_install_prefix:

cmake_install_prefix
--------------------
The actual prefix used for the install is

| |tab| *cmake_install_prefix.build_type*

and a soft link is created from *cmake_install_prefix* to this directory.

.. meta::
   :keywords: build

.. index:: build

.. _get_cppad_sh@Settings@build_type@build:

build
-----
The subdirectory

| |tab| ``build.``\ *build_type*

is used to compile and test the software and a soft link is created from
``build`` to this subdirectory.

.. meta::
   :keywords: include_mixed

.. index:: include_mixed

.. _get_cppad_sh@Settings@include_mixed:

include_mixed
=============
This flag is true (false) if we are (are not)
including the python cppad_mixed interface.

.. literalinclude:: ../bin/get_cppad.sh
   :lines: 88-88
   :language: sh

If it is true, the install script ``bin/get_cppad_mixed.sh``
should be used to install Cppad together with the all the other cppad_mixed
requirements.
Otherwise, ``bin/get_cppad.sh`` should be used to install Cppad.

.. meta::
   :keywords: test_cppad

.. index:: test_cppad

.. _get_cppad_sh@Settings@test_cppad:

test_cppad
==========
This must be must ``true`` or ``false`` .
Cppad has a huge test suite and this can take a significant amount of time,
but it may be useful if you have problems.

.. literalinclude:: ../bin/get_cppad.sh
   :lines: 101-101
   :language: sh

.. meta::
   :keywords: caching

.. index:: caching

.. _get_cppad_sh@Caching:

Caching
*******
This script and ``bin/get_cppad_mixed.sh`` cache previous builds so that
when you re-run the script it does not re-do all the work.
If you have trouble, try deleting the directory

| |tab| ``build/external``

and re-running this script.
