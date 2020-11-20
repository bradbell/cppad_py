!!!!!!!!!!!!
get_cppad_sh
!!!!!!!!!!!!

.. include:: ../preamble.rst

.. meta::
   :keywords: get_cppad_sh, get, cppad

.. index:: get_cppad_sh, get, cppad

.. _get_cppad_sh:

Get Cppad
#########
.. contents::
   :local:

.. meta::
   :keywords: syntax

.. index:: syntax

.. _get_cppad_sh.syntax:

Syntax
******
``bin/get_cppad.sh``

.. meta::
   :keywords: top, source, directory

.. index:: top, source, directory

.. _get_cppad_sh.top_source_directory:

Top Source Directory
********************
This program must be run from the
:ref:`top_source_directory<setup_py.download.top_source_directory>`.

.. meta::
   :keywords: settings

.. index:: settings

.. _get_cppad_sh.settings:

Settings
********
If you change any of these settings, you must re-run ``get_cppad.sh`` .

.. meta::
   :keywords: cmake_install_prefix

.. index:: cmake_install_prefix

.. _get_cppad_sh.settings.cmake_install_prefix:

cmake_install_prefix
====================
This prefix is used to install cppad_py. It may be a local directory; e.g.,
``build/prefix`` or an absolute path; e.g., ``/usr/local``.
It may include the shell variable ``$HOME`` but no other variables:

.. code-block:: sh

    cmake_install_prefix="$HOME/prefix/cppad"

If this prefix does no start with ``/``, it is relative to the
:ref:`top_source_directory<setup_py.download.top_source_directory>`.
Note that ``$HOME`` starts with ``/``.

.. meta::
   :keywords: extra_cxx_flags

.. index:: extra_cxx_flags

.. _get_cppad_sh.settings.extra_cxx_flags:

extra_cxx_flags
===============
Extra compiler flags used when compiling c++ code not including the
debugging and optimization flags.
The ones below are example flags are used by g++:

.. code-block:: sh

    extra_cxx_flags='-Wall -pedantic-errors -Wno-unused-result -std=c++11'

.. meta::
   :keywords: build_type

.. index:: build_type

.. _get_cppad_sh.settings.build_type:

build_type
==========
This must be must ``debug`` or ``release`` .
The debug version has more error messaging while the release
version runs faster.

.. code-block:: sh

    build_type='release'

.. meta::
   :keywords: cmake_install_prefix

.. index:: cmake_install_prefix

.. _get_cppad_sh.settings.build_type.cmake_install_prefix:

cmake_install_prefix
--------------------
The actual prefix used for the install is

| |tab| *cmake_install_prefix.build_type*

and a soft link is created from *cmake_install_prefix* to this directory.

.. meta::
   :keywords: build

.. index:: build

.. _get_cppad_sh.settings.build_type.build:

build
-----
The subdirectory

| |tab| ``build.``\ *build_type*

is used to compile and test the software and a soft link is created from
``build`` to this subdirectory.

.. meta::
   :keywords: include_mixed

.. index:: include_mixed

.. _get_cppad_sh.settings.include_mixed:

include_mixed
=============
This flag is true (false) if we are (are not)
including the python cppad_mixed interface.

.. code-block:: sh

    include_mixed='false'

If it is true, the install script ``bin/get_cppad_mixed.sh``
should be used to install Cppad together with the all the other cppad_mixed
requirements.
Otherwise, ``bin/get_cppad.sh`` should be used to install Cppad.

.. meta::
   :keywords: test_cppad

.. index:: test_cppad

.. _get_cppad_sh.settings.test_cppad:

test_cppad
==========
This must be must ``true`` or ``false`` .
Cppad has a huge test suite and this can take a significant amount of time,
but it may be useful if you have problems.

.. code-block:: sh

    test_cppad='false'

.. meta::
   :keywords: caching

.. index:: caching

.. _get_cppad_sh.caching:

Caching
*******
This script and ``bin/get_cppad_mixed.sh`` cache previous builds so that
when you re-run the script it does not re-do all the work.
If you have trouble, try deleting the directory

| |tab| ``build/external``

and re-running this script.

----

xsrst input file: ``bin/get_cppad.sh``
