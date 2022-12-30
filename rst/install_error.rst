.. _install_error-name:

!!!!!!!!!!!!!
install_error
!!!!!!!!!!!!!

.. raw:: html

   <a href="_sources/install_error.rst.txt">View page source</a>

.. meta::
   :keywords: install_error, error, messages, during, installation

.. index:: install_error, error, messages, during, installation

.. _install_error-title:

Error Messages During Installation
##################################

.. meta::
   :keywords: get_cppad_mixed.sh

.. index:: get_cppad_mixed.sh

.. _install_error@get_cppad_mixed.sh:

get_cppad_mixed.sh
******************
On Mac OS the following error messages may appear while running
``bin/get_cppad_mixed.sh`` :

.. meta::
   :keywords: java

.. index:: java

.. _install_error@get_cppad_mixed.sh@Java:

Java
====
| |tab| ``To use javac command-line tool you need to install a JDK.``

This indicates that you have not added
the location where brew installs openjdk to you execution path.
Try executing the command

| |tab| ``PATH="/usr/local/opt/openjdk/bin:$PATH"``

.. meta::
   :keywords: cholmod.h

.. index:: cholmod.h

.. _install_error@get_cppad_mixed.sh@cholmod.h:

cholmod.h
=========
| |tab| ``cannot find cholmod.h``

The suitesparse package does not have pkg-config support,
hence cppad_mixed searches a set of directories for ``cholmod.h``
(which is part of suitesparse).
It you get this message, find out where ``cholmod.h`` is installed
on your system and open an issue about this on the
`cppad_py issues <https://github.com/bradbell/cppad_py/issues>`_ page.

---------------------------------------------------------------------------

.. meta::
   :keywords: setup.py

.. index:: setup.py

.. _install_error@setup.py:

setup.py
********
The following error messages may appear
while running ``setup.py`` :

.. meta::
   :keywords: swig

.. index:: swig

.. _install_error@setup.py@swig:

swig
====
| |tab| ``FileNotFoundError: [Errno 2] No such file or directory: 'swig'``

Try installing `swig <http://www.swig.org/>`_ on you system.

.. meta::
   :keywords: cppad.pc,, cppad_mixed.pc

.. index:: cppad.pc,, cppad_mixed.pc

.. _install_error@setup.py@cppad.pc, cppad_mixed.pc:

cppad.pc, cppad_mixed.pc
========================
| |tab| ``Cannot find`` *name*\ ``.pc``

where *name* is ``cppad`` or ``cppad_mixed``.
You probably did not set
:ref:`PKG_CONFIG_PATH <setup_py@PKG_CONFIG_PATH>` correctly.

.. meta::
   :keywords: symbolic, link

.. index:: symbolic, link

.. _install_error@setup.py@symbolic link:

symbolic link
=============
| |tab| ``build_type.sh:`` *prefix*  ``is not a symbolic link``

where *prefix* is the
:ref:`get_cppad_sh@Settings@cmake_install_prefix` in ``bin/get_cppad.sh``.
Try removing the *prefix* directory and re-running setup.py.

.. meta::
   :keywords: fortify, source

.. index:: fortify, source

.. _install_error@setup.py@Fortify Source:

Fortify Source
==============
| |tab| ``#warning _FORTIFY_SOURCE requires compiling with optimization``

This is a problem with the python setuptools,
one can un-define a macro, but it does not remove a original definition.
It only happens when :ref:`build_type<get_cppad_sh@Settings@build_type>`
to ``debug`` .

.. meta::
   :keywords: stdio.h

.. index:: stdio.h

.. _install_error@setup.py@stdio.h:

stdio.h
=======
| |tab| ``'stdio.h' file not found``

This is a problem with the Mac system and the solutions keep changing; see
`stdio.h <https://stackoverflow.com/questions/19580758/gcc-fatal-error-stdio-h-no-such-file-or-directory>`_

If the solutions in the link above do not work
and you are using ``brew``,
try using brew to install python3.
Then add the location where brew installs python libraries
to you execution path :

| |tab| ``minor=$(echo "import sys;print(sys.version_info.minor)" | python3)``
| |tab| ``PATH="/usr/local/opt/python@3.$minor/bin:$PATH"``

If your are using ``port`` , try the following :

| |tab| ``minor=$(echo "import sys;print(sys.version_info.minor)" | python3)``
| |tab| ``"/opt/local/Library/Frameworks/Python.framework/Versions/3.$minor/bin:$PATH"``

---------------------------------------------------------------------------

.. meta::
   :keywords: check_all.py

.. index:: check_all.py

.. _install_error@check_all.py:

check_all.py
************
The following error messages may appear
while running ``python3 example/python/check_all.py`` :

.. meta::
   :keywords: numpy,, scipy

.. index:: numpy,, scipy

.. _install_error@check_all.py@numpy, scipy:

numpy, scipy
============
| |tab| ``module`` *name* ``has no attribute`` ...

where *name* is ``numpy`` or ``scipy``.
Try installing *name* using the command

| |tab| ``pip3 install`` *name*

.. meta::
   :keywords: cppad_py

.. index:: cppad_py

.. _install_error@check_all.py@cppad_py:

cppad_py
========
| |tab| ``ModuleNotFoundError: No module named cppad_py``

This means that the ``cppad_py`` directory can't be found.
If you are testing the local copy, make sure that the directory

| |tab| *top_src*\ ``/cppad_py``

exists; see :ref:`local build <setup_py@Local Build>` .
If you are testing the installed version, make sure the directory

| |tab| ``$PYTHONPATH/cppad_py``

exists; see :ref:`PYTHONPATH <setup_py@PYTHONPATH>` .

.. meta::
   :keywords: libcppad_lib

.. index:: libcppad_lib

.. _install_error@check_all.py@libcppad_lib:

libcppad_lib
============
| |tab| ``ImportError: libcppad_lib.so`` ... ``can not open shared object file``

This means the CppAD library
is not in your :ref:`LD_LIBRARY_PATH<setup_py@LD_LIBRARY_PATH>` .
If you have a Mac, you will instead need to set ``DYLD_LIBRARY_PATH`` .
