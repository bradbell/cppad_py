.. _setup_py-name:

!!!!!!!!
setup_py
!!!!!!!!

.. raw:: html

   <a href="_sources/setup_py.rst.txt">View page source</a>

.. meta::
   :keywords: setup_py, configure, build, the, cppad_py, python, module

.. index:: setup_py, configure, build, the, cppad_py, python, module

.. _setup_py-title:

Configure and Build the cppad_py Python Module
##############################################

.. meta::
   :keywords: syntax

.. index:: syntax

.. _setup_py@Syntax:

Syntax
******

| ``python3 setup.py install --prefix=``\ *prefix*

.. meta::
   :keywords: external, requirements

.. index:: external, requirements

.. _setup_py@External Requirements:

External Requirements
*********************
#. `bash <https://en.wikipedia.org/wiki/Bash_(Unix_shell)>`_
#. `cmake <https://cmake.org>`_
#. `swig <http://www.swig.org/>`_
#. `c++ <https://en.wikipedia.org/wiki/C++>`_
#. `git <https://git-scm.com/>`_
#. `pkg-config <https://www.freedesktop.org/wiki/Software/pkg-config>`_
#. `python <https://www.python.org/>`_ version 3
#. `python-numpy <https://numpy.org/>`_
#. `python-scipy <https://scipy.org/>`_
#. `python-setuptools <https://scipy.org/>`_

.. meta::
   :keywords: include, mixed, effects, modeling

.. index:: include, mixed, effects, modeling

.. _setup_py@External Requirements@Include Mixed Effects Modeling:

Include Mixed Effects Modeling
==============================
If :ref:`get_cppad_sh@Settings@include_mixed` is true,
the external packages listed below are also required.
Note that, for most cases, ``get_cppad_mixed.sh``
will get all the required packages.

#. The `wget <https://www.gnu.org/software/wget>`_ program.
#. A fortran compiler.
#. The `gsl <http://gnuwin32.sourceforge.net/packages/gsl.htm>`_ library
   including its development headers.
#. `suitesparse <http://faculty.cse.tamu.edu/davis/SuiteSparse%suitesparse>`_
   package. Note that only cholmod is really required from suitesparse.

.. meta::
   :keywords: download

.. index:: download

.. _setup_py@Download:

Download
********
Use the following command to download the current version of cppad_py:

| |tab| ``git clone https://github.com/bradbell/cppad_py.git`` *top_srcdir*

.. meta::
   :keywords: top, source, directory

.. index:: top, source, directory

.. _setup_py@Download@Top Source Directory:

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

.. _setup_py@Configure:

Configure
*********
Before running ``setup_py`` or ``bin/get_cppad.sh`` ,
you should check and possibly change the
:ref:`settings<get_cppad_sh@Settings>` in ``bin/get_cppad.sh`` .

.. meta::
   :keywords: get, cppad

.. index:: get, cppad

.. _setup_py@Get cppad:

Get cppad
*********
The next step is to get a copy of cppad using
:ref:`get_cppad_sh-name`.
If you want to use the :ref:`mixed-title` class, you will have to set
:ref:`include_mixed<get_cppad_sh@Settings@include_mixed>` to true
and use ``bin/get_cppad_mixed.sh`` to install cppad and other
non-standard requirements.

.. meta::
   :keywords: prefix

.. index:: prefix

.. _setup_py@prefix:

prefix
******
We use *prefix* to denote the prefix where cppad_py will be installed.
This is the same as the value of
:ref:`cmake_install_prefix<get_cppad_sh@Settings@cmake_install_prefix>` .
You can create a variable with this value using the command

| |tab| ``cmd=$(grep '^cmake_install_prefix=' bin/get_cppad.sh)``
| |tab| ``eval $cmd``
| |tab| ``prefix="$cmake_install_prefix"``

.. meta::
   :keywords: libdir

.. index:: libdir

.. _setup_py@libdir:

libdir
******
The value *libdir* is the suffix (after the prefix)
where the libraries will be installed.
This can be determined by running the command:

.. literalinclude:: ../../setup.py
   :lines: 386-386
   :language: sh

You can create a variable with this value using the command

| |tab| ``libdir=$(bin/libdir.py)``

.. meta::
   :keywords: ld_library_path

.. index:: ld_library_path

.. _setup_py@LD_LIBRARY_PATH:

LD_LIBRARY_PATH
***************
Make sure the directory *prefix/libdir*
is in your ``LD_LIBRARY_PATH``
For example, if you set *prefix* and *libdir* as above,

| |tab| ``export LD_LIBRARY_PATH=$prefix/$libdir``

In mac OS ``LD_LIBRARY_PATH`` should be replaced by ``DYLD_LIBRARY_PATH`` .
For example,

| |tab| ``export DYLD_LIBRARY_PATH=$prefix/$libdir``

In msys2 and cygwin you do not need to set ``LD_LIBRARY_PATH`` because
static, instead of dynamic, libraries are used.

.. meta::
   :keywords: pkg_config_path

.. index:: pkg_config_path

.. _setup_py@PKG_CONFIG_PATH:

PKG_CONFIG_PATH
***************
Make sure the directory *prefix/libdir/*\ ``pkgconfig``
is in your ``PKG_CONFIG_PATH``.
For example,

| |tab| ``export PKG_CONFIG_PATH=$prefix/$libdir/pkgconfig``

.. meta::
   :keywords: local, build

.. index:: local, build

.. _setup_py@Local Build:

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

.. _setup_py@Local Test:

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

.. _setup_py@PYTHONPATH:

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

.. _setup_py@Install:

Install
*******
Use the following command to build and install cppad_py:

| |tab| ``python3 setup.py install --prefix=$prefix``

(see :ref:`prefix<setup_py@prefix>` above for how to set this shell
variable).

This will install cppad_py in the directory

| |tab| *prefix/libdir*\ ``/python3.``\ *minor* ``/site-packages/cppad_py``

.. meta::
   :keywords: test, install

.. index:: test, install

.. _setup_py@Test Install:

Test Install
************
You can test the installed version by executing the command

| |tab| ``python3 example/python/check_all.py``

If the directory *top_srcdir/*\ ``cppad_py`` exists,
you will be testing the local version, instead of the installed version.
If this directory exists when the install command is run,
it is removed by the install command.

.. meta::
   :keywords: mac, os

.. index:: mac, os

.. _setup_py@Mac Os:

Mac Os
******
The Mac Os system has only been tested using
`brew <https://brew.sh>`_  and
`port <https://www.macports.org>`_
to install packages not included with the system.

.. meta::
   :keywords: cygwin

.. index:: cygwin

.. _setup_py@Cygwin:

Cygwin
******
A cygwin install, on 2021-05-06 and with
:ref:`include_mixed<get_cppad_sh@Settings@include_mixed>` false,
completed successfully by doing the following:
First the following packages were added to the default set installed by the
cygwin ``setup-x86_64`` program:
gcc-core, gcc-g++, gcc-fortran,
python3-devel, python-pip-wheel, python-setuptools-wheel,
lapack-devel, libopenblas,
git, vim, cmake, make, swig.
Then the ``pip3`` program was used to install numpy and scipy.
Then the install instructions above were used to install and test
cppad_py.

.. meta::
   :keywords: msys2

.. index:: msys2

.. _setup_py@Msys2:

Msys2
*****
A msys2 install with,
:ref:`include_mixed<get_cppad_sh@Settings@include_mixed>` false,
was attempted on 2021-05-09.
First the following packages were installed using pacman:
vim, git, make, cmake, swig.
Next the mingw-w64-x86_64 version of following packages were installed using
pacman:  python, python-scipy, python-setuptools, gcc
The problem is that setup.py is mixing windows and unix paths.
An attempt was made to fix the environment variables using ``cygpath``
utility, but other related problems still persisted.

.. meta::
   :keywords: children

.. index:: children

.. _setup_py@Children:

Children
********

.. csv-table::
   :header:  "Child", "Title"
   :widths: auto

   "install_error", :ref:`install_error-title`
   "get_cppad_sh", :ref:`get_cppad_sh-title`
   "get_cppad_mixed_sh", :ref:`get_cppad_mixed_sh-title`

.. toctree::
   :maxdepth: 1
   :hidden:

   install_error
   get_cppad_sh
   get_cppad_mixed_sh
