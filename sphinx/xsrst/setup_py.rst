!!!!!!!!
setup_py
!!!!!!!!

.. toctree::
   :maxdepth: 1
   :hidden:

   install_error
   get_cppad_sh

.. include:: ../preamble.rst

.. meta::
   :keywords: setup_py, configure, build, the, cppad_py, python, module

.. index:: setup_py, configure, build, the, cppad_py, python, module

.. _setup_py:

Configure and Build the cppad_py Python Module
##############################################
.. contents::
   :local:

.. meta::
   :keywords: syntax

.. index:: syntax

.. _setup_py.syntax:

Syntax
******

| ``python3 setup.py install --prefix=``\ *prefix*

.. meta::
   :keywords: external, requirements

.. index:: external, requirements

.. _setup_py.external_requirements:

External Requirements
*********************
#. `bash <https://en.wikipedia.org/wiki/Bash_(Unix_shell)>`_
#. `python <https://www.python.org/>`_ version 3
#. `numpy <https://numpy.org/>`_
#. `scipy <https://scipy.org/>`_
#. `cmake <https://cmake.org>`_
#. `swig <http://www.swig.org/>`_
#. `c++ <https://en.wikipedia.org/wiki/C++>`_
#. `git <https://git-scm.com/>`_
#. `pkg-config <https://www.freedesktop.org/wiki/Software/pkg-config>`_

.. meta::
   :keywords: mac, os

.. index:: mac, os

.. _setup_py.external_requirements.mac_os:

Mac Os
======
The Mac Os system has only been tested using
`brew <https://brew.sh>`_  and
`port <https://www.macports.org>`_
to install packages not included with the system.

.. meta::
   :keywords: download

.. index:: download

.. _setup_py.download:

Download
********
Use the following command to download the current version of cppad_py:

| |tab| ``git clone https://github.com/bradbell/cppad_py.git`` *top_srcdir*

.. meta::
   :keywords: top, source, directory

.. index:: top, source, directory

.. _setup_py.download.top_source_directory:

Top Source Directory
====================
The directory you choose for *top_srcdir* is
referred to as your *top_srcdir* directory.
We suggest you use ``cppad_py.git`` for my *top_srcdir*
so it is different from the ``cppad_py`` directory
created by the instructions below.

.. meta::
   :keywords: configure

.. index:: configure

.. _setup_py.configure:

Configure
*********
Before running ``setup_py`` or ``bin/get_cppad.sh`` ,
you should check and possibly change the
:ref:`settings<get_cppad_sh.settings>` in ``bin/get_cppad.sh`` .

.. meta::
   :keywords: get, cppad

.. index:: get, cppad

.. _setup_py.get_cppad:

Get cppad
*********
The next step is to get a copy of cppad using
:ref:`get_cppad_sh<get_cppad_sh>`.
If you want to use the :ref:`mixed` class, you will have to set
:ref:`include_mixed<get_cppad_sh.settings.include_mixed>` to true
and use ``bin/get_cppad_mixed.sh`` to install cppad and other
non-standard requirements.

.. meta::
   :keywords: prefix

.. index:: prefix

.. _setup_py.prefix:

prefix
******
We use *prefix* to denote the prefix where cppad_py will be installed.
This is the same as the value of
:ref:`cmake_install_prefix<get_cppad_sh.settings.cmake_install_prefix>` .
You can create a variable with this value using the command

| |tab| ``cmd=$(grep '^cmake_install_prefix=' bin/get_cppad.sh)``
| |tab| ``eval $cmd``
| |tab| ``prefix="$cmake_install_prefix"``

.. meta::
   :keywords: libdir

.. index:: libdir

.. _setup_py.libdir:

libdir
******
The value *libdir* is the suffix (after the prefix)
where the libraries will be installed.
This can be determined by running the command:

.. code-block:: sh

      bin/libdir.py ; echo

You can create a variable with this value using the command

| |tab| ``libdir=$(bin/libdir.py)``

.. meta::
   :keywords: ld_library_path

.. index:: ld_library_path

.. _setup_py.ld_library_path:

LD_LIBRARY_PATH
***************
Make sure the directory *prefix/libdir*
is in your ``LD_LIBRARY_PATH``
For example, if you set *prefix* and *libdir* as above,

| |tab| ``export LD_LIBRARY_PATH=$prefix/$libdir``

In mac OS ``LD_LIBRARY_PATH`` should be replaced by ``DYLD_LIBRARY_PATH`` .
For example,

| |tab| ``export DYLD_LIBRARY_PATH=$prefix/$libdir``

.. meta::
   :keywords: pkg_config_path

.. index:: pkg_config_path

.. _setup_py.pkg_config_path:

PKG_CONFIG_PATH
***************
Make sure the directory *prefix/libdir/*\ ``pkgconfig``
is in your ``PKG_CONFIG_PATH``.
For example,

| |tab| ``export PKG_CONFIG_PATH=$prefix/$libdir/pkgconfig``

.. meta::
   :keywords: local, build

.. index:: local, build

.. _setup_py.local_build:

Local Build
***********
You should first remove any previous local copy of the Python cppad_py
module (that might exist) using the command

| |tab| ``rm -r build/lib.*``

You can build a local copy of the Python cppad_py module using the
following command in the *top_srcdir* :

| |tab| ``python3 setup.py bdist``

This will create the directory

| |tab| ``build/lib.``\ *name*\ ``/cppad_py``

where *name* identifies your system and version of python.
For example, you can set a variable equal to the value of *name*
by executing the command

| |tab| ``name=$(ls build | grep '^lib\.' | sed -e 's|^lib\.||')``

The next step is to copy the ``cppad_py`` directory to the
*top_srcdir* . For example,

| |tab| ``cp -r build/lib.$name/cppad_py cppad_py``

.. meta::
   :keywords: local, test

.. index:: local, test

.. _setup_py.local_test:

Local Test
**********
You can test the local copy by executing the following commands in the
*top_srcdir* directory:

| |tab| ``PYTHONPATH=""``
| |tab| ``python3 example/python/check_all.py``

This test will use the local copy of *top_srcdir/*\ ``cppad_py``
create by the local build instructions directly above.

.. meta::
   :keywords: pythonpath

.. index:: pythonpath

.. _setup_py.pythonpath:

PYTHONPATH
**********
In order to use the installed version of cppad_py,
you must add the directory

| |tab| *prefix/libdir*\ ``/python3.``\ *minor*\ ``/site-packages``

to your ``PYTHONPATH``
where *minor* is the minor version corresponding to ``python3``.
For example,

| |tab| ``minor=$(echo "import sys;print(sys.version_info.minor)" | python3)``
| |tab| ``export PYTHONPATH=$prefix/$libdir/python3.$minor/site-packages``

.. meta::
   :keywords: install

.. index:: install

.. _setup_py.install:

Install
*******
Use the following command to build and install cppad_py:

| |tab| ``python3 setup.py install --prefix=$prefix``

(see :ref:`prefix<setup_py.prefix>` above for how to set this shell
variable).

This will install cppad_py in the directory

| |tab| *prefix/libdir*\ ``/python3.``\ *minor* ``/site-packages/cppad_py``

.. meta::
   :keywords: test, install

.. index:: test, install

.. _setup_py.test_install:

Test Install
************
You can test the installed version by executing the command

| |tab| ``python3 example/python/check_all.py``

If the directory *top_srcdir/*\ ``cppad_py`` exists,
you will be testing the local version, instead of the installed version.
If this directory exists when # the install command is run,
it is removed by the install command.

.. meta::
   :keywords: install, errors

.. index:: install, errors

.. _setup_py.install_errors:

Install Errors
**************
If you get an error message during the install procedure above,
or the one below, see :ref:`install_error<install_error>`.
This will only install the release version.
Installing a debug version is discussed below in the instructions
for downloading and building from the source code.

.. meta::
   :keywords: install, using, pip

.. index:: install, using, pip

.. _setup_py.install_using_pip:

Install Using Pip
*****************
There is an old version of cppad_py available using ``pip`` .
To install for you entire system use:

| |tab| ``pip install -i https://test.pypi.org/simple/ cppad_py``

.. meta::
   :keywords: children

.. index:: children

.. _setup_py.children:

Children
********
.. csv-table::
    :header:  "Name", "Title"
    :widths: 20, 80

    "install_error", :ref:`install_error`
    "get_cppad_sh", :ref:`get_cppad_sh`

----

xsrst input file: ``setup.py``
