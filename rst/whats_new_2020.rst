.. _whats_new_2020-name:

!!!!!!!!!!!!!!
whats_new_2020
!!!!!!!!!!!!!!

.. raw:: html

   <a href="_sources/whats_new_2020.rst.txt">View page source</a>

.. meta::
   :keywords: whats_new_2020, cppad, py, changes, during, 2020

.. index:: whats_new_2020, cppad, py, changes, during, 2020

.. _whats_new_2020-title:

CppAD Py Changes During 2020
############################

.. _whats_new_2020@12-01:

12-01
*****
#. Advance to cppad_mixed-20201130.
   This fixes a problem installing on the Mac with port.
   To be specific, the directory ``/opt/local`` is searched
   when looking for ``cholmod.h`` .
   It also gives better error messaging during the install procedure.
#. Group the install error messages under the program being run;
   i.e., :ref:`install_error@get_cppad_mixed.sh` ,
   i.e., :ref:`install_error@setup.py` ,
   i.e., :ref:`install_error@check_all.py` .
#. Added a discussion of the :ref:`install_error@get_cppad_mixed.sh@cholmod.h`
   error message.

.. _whats_new_2020@11-20:

11-20
*****
#. Add the :ref:`f@check_for_nan <py_fun_check_for_nan-name>` and
   :ref:`a_double_binary@pow_int` functions.
#. CppAD errors were not being translated to python exceptions
   (except for :ref:`mixed <mixed-name>` class operations).
   This has been fixed; see :ref:`cppad_error-title` .
#. More error detection and reporting when numpy vectors
   or matrices do not have the correct dimensions.

.. _whats_new_2020@11-19:

11-19
*****
Advance to cppad_mixed-20201119. Also make version of cppad
installed by bin/get_cppad.sh the same as by bin/get_cppad_mixed.sh .

.. _whats_new_2020@11-18:

11-18
*****
#. Advance to cppad_mixed-2020118. This adds support for
   mac using `port <https://www.macports.org>`_ to install packages.
   The previous version assumed the mac was using
   `brew <https://brew.sh>`_ to install packages.
#. Add a :ref:`install_error@setup.py@symbolic link` and
   :ref:`install_error@setup.py@cppad.pc, cppad_mixed.pc` entries to the
   list of install error messages.
#. Remove under construction from the :ref:`mixed-title` class; i.e.,
   it has reached a stable state.
#. Make a separate definition for the random and
   :ref:`mixed@Notation@Fixed Effects Likelihood`.
#. Fix the definition of
   :ref:`mixed_ctor@fixed_init@n_fixed` and
   :ref:`mixed_ctor@random_init@n_random`.

.. _whats_new_2020@11-17:

11-17
*****
#. The :ref:`setup@py <setup_py-name>` script was improved.
   To be specific:

      -  The :ref:`covid 19 example <numeric_covid_19_xam_py-name>` was removed
         from the automatic testing because it is slow.
      -  The python matplotlib module is no longer required because is was
         only used by the covid 19 example.
      -  Separate headings were created for
         :ref:`local testing <setup_py@Local Test>` and
         :ref:`install testing <setup_py@Test Install>`.

#. The ``PyEval_CallObject`` function was deprecated in python3.9.
   It's use was converted to ``PyObject_CallObject`` to avoid this warning.

.. _whats_new_2020@11-16:

11-16
*****
#. **API change**: the :ref:`pat <py_sparse_rcv@pat>` member function
   was added to the ``sparse_rcv`` class and the constructor was change to
   have no arguments. The old syntax

   | |tab| *matrix* = ``cppad_py.sparse_rcv`` ( *pattern* )

   will need to be changed to

   | |tab| *matrix* = ``cppad_py.sparse_rcv()``
   | |tab| *matrix*\ ``.pat`` ( *pattern* )

#. The :ref:`hes_fixed_obj <mixed_hes_fixed_obj-name>` mixed class member function
   syntax was changed to make the result an argument instead of return value.
   This avoids having to make an extra copy of the sparse matrix.
#. Add :ref:`hes_random_obj <mixed_hes_random_obj-name>`
   to the mixed class operations.

.. _whats_new_2020@11-15:

11-15
*****
#. Fix a memory leak in the destructor for a
   :ref:`d_fun <py_fun_ctor@Syntax@d_fun>` object.
#. The syntax for the c++ :ref:`sparse_rcv <cpp_sparse_rcv-name>`
   and :ref:`sparse_rcv <cpp_sparse_rcv-name>` constructors has changed.
   To be specific, they no longer use the assignment operator ``=`` .
#. Add the word ``destructor`` to the xrst dictionary.
#. Add :ref:`hes_fixed_obj <mixed_hes_fixed_obj-name>`
   to the mixed class operations.

.. _whats_new_2020@11-14:

11-14
*****
Add :ref:`optimize_random <mixed_optimize_random-name>`
to the mixed class operations.

.. _whats_new_2020@11-12:

11-12
*****
#. Improve the :ref:`ipopt options
   <mixed_optimize_fixed@fixed_ipopt_options@ipopt options>` documentation.
#. Fix the font in the syntax for the rosen3_step functions
   :ref:`f <numeric_rosen3_step@fun@f>` ,
   :ref:`f_t <numeric_rosen3_step@fun@f_t>` , and
   :ref:`f_y <numeric_rosen3_step@fun@f_y>` .
#. Remove some extra space when a '.' character appears between the
   change between italic and literal font.
#. Add an install error entry for when the
   :ref:`cppad_py <install_error@check_all.py@cppad_py>`
   module can't be found.

.. _whats_new_2020@11-11:

11-11
*****
Improve the install instructions in :ref:`setup_py-name`
and :ref:`install_error-name`.

.. _whats_new_2020@11-10:

11-10
*****
#. **API change** : the xrst ``child_list`` command was changed to
   child_table and a table,
   instead of a list, was used to display the names and corresponding titles.
   In addition, the ``child_link`` command was changed to
   child_list.
#. Remove an extra backquote \' that was placed at the end of each line
   of the :ref:`xrst_table_of_contents-title`.
#. Add more documentation for the ``index.rst`` file
   (including how to link to the table of contents).
#. The java runtime environment as add to the install
   :ref:`requirements<setup_py@External Requirements>`.

.. _whats_new_2020@11-08:

11-08
*****
#. Change setup.py :ref:`local build<setup_py@Local Build>` and test instructions so they work on Mac OS.

#. Fix ``bin/get_cppad_mixed.sh`` so that it is not necessary to set
   LD_LIBRARY_PATH or PKG_CONFIG_PATH before running it.

#. Where appropriate, reduce the spacing between italic and literal font; e.g.,

   | |tab| *prefix/libdir* ``/python3.`` *minor* ``/site-packages/cppad_py``

   was changed to

   | |tab| *prefix/libdir*\ ``/python3.``\ *minor* ``/site-packages/cppad_py``

.. _whats_new_2020@11-06:

11-06
*****
#. The install with
   :ref:`include_mixed<get_cppad_sh@Settings@include_mixed>` false was broken
   by the changes on 11-03. This has been fixed.

#. The installation and testing instructions in :ref:`setup@py<setup_py-name>`
   were brought up to date and improved.
   This includes discussion of the following environment variables:
   :ref:`LD_LIBRARY_PATH<setup_py@LD_LIBRARY_PATH>`,
   :ref:`PKG_CONFIG_PATH<setup_py@PKG_CONFIG_PATH>`,
   :ref:`PYTHONPATH<setup_py@PYTHONPATH>`.

#. The setting *cppad_lib* was changed to the automatically determined
   value :ref:`libdir<setup_py@libdir>`.

.. _whats_new_2020@11-05:

11-05
*****
Advance to cppad_mixed-20201105.
This fixes some problems with it's install in Mac OS.

.. _whats_new_2020@11-04:

11-04
*****
The install prefix for cppad in ``bin/get_cppad.sh``
is called *cmake_install_prefix* in cppad_py,
but it is called *cppad_prefix* in cppad.
The cmake command in ``bin/get_cppad.sh`` has been
fixed to account for this.

.. _whats_new_2020@11-03:

11-03
*****
The install prefix name was changed from *cppad_prefix* to
:ref:`cmake_install_prefix<get_cppad_sh@Settings@cmake_install_prefix>`.

.. _whats_new_2020@10-31:

10-31
*****
Fix some problems with the macOS install when
:ref:`include_fixed<get_cppad_sh@Settings@include_mixed>` is true.

.. _whats_new_2020@10-30:

10-30
*****
The :ref:`install command<setup_py@Install>` no longer creates
a local copy of ``cppad_py`` for testing. (On macOS systems the
local copy would cause problems during the install.)
The :ref:`setup_py@Local Build` still builds the local
copy for testing.

.. _whats_new_2020@10-29:

10-29
*****
#. The *cppad_libdir* setting was added to ``bin/get_cppad.sh``.
   This fixed a problem on some systems where ``bin/get_cppad.sh``
   and ``bin/get_cppad_mixed.sh`` might install the cppad library
   in two different locations and confuse the setup procedure.

#. Fix a problem with ``setup.py`` where it sometimes puts the distribution
   in ``site-packages/cppad_py-`` *version* ``.egg/cppad_py`` instead of
   ``site-packages/cppad_py``. This may have something to do with the
   install egg being a directory instead of a zip file.

.. _whats_new_2020@10-28:

10-28
*****
#. Improve the :ref:`setup@py<setup_py-name>` install instructions.
   To be specific, change ``python`` to ``python3`` and edit the
   :ref:`external requirements<setup_py@External Requirements>`.

#. Improve the :ref:`get_cppad_sh-title` script so that it gets and updates
   posted to the remote repository (since the previous run of the script).

.. _whats_new_2020@10-21:

10-21
*****
#. Add a second :ref:`optimize_fixed example<mixed_optimize_fixed@Examples>`.

#. Advance to cppad-20201021 (this fixes a warning on some compilers).

.. _whats_new_2020@10-19:

10-19
*****
Add the non linear constraint functions of the fixed effects
to the mixed class; see :ref:`mixed_fix_constraint-title`.

.. _whats_new_2020@10-17:

10-17
*****
#. The default value (corresponding to ``None``)
   for :ref:`mixed_optimize_fixed@fixed_in (random_in)` in ``optimize_fixed``
   was changed from zero to *fixed_init* (*random_init*).
   The :ref:`mixed_ran_likelihood_xam_py-title` example was changed to use this
   default.

#. There was a problem linking the needed libraries when
   :ref:`include_mixed<get_cppad_sh@Settings@include_mixed>` was true.
   This has been fixed.

#. A ``match_op.hpp`` warning was added to the
   install errors section (it has since been removed).

#. The :ref:`numpy syntax<a_double_unary_fun@Syntax@Python>` was added
   to the documentation python syntax for ``a_double`` unary functions;
   for an example see :ref:`a_double_unary_fun_xam_py-title`.

.. _whats_new_2020@10-16:

10-16
*****
#. Add the :ref:`mixed-title` class an make it optional during the install process;
   see :ref:`include_mixed<get_cppad_sh@Settings@include_mixed>`.
   This class is under construction and its API may change.
   Check this page for such changes.

#. Change the install process so both a debug and release version of
   :ref:`cmake_install_prefix<get_cppad_sh@Settings@build_type@cmake_install_prefix>`
   can be installed at the same time.

#. Some of the install steps in :ref:`setup_py-title` have changed.

.. _whats_new_2020@10-13:

10-13
*****
The xrst.py utility would crash if a section had child_cmd
and was indented.
This has been fixed

.. _whats_new_2020@10-02:

10-02
*****
#. The library documentation that is for both c++ and python was improved.
   To be specific, both the c++ and python syntax was included.
   Also these sections were moved from children of :ref:`cpp_lib-title`
   to children of :ref:`library-title`.

#. The xrst.py utility has been improved. To be specific, it no
   longer overwrites ``*.rst`` files that have not changed. This makes
   the sphinx build operation faster (by not reprocessing files
   that have not changed).

#. Use the 95% quantile, instead of maximum, absolute residual when
   testing simulated fit in :ref:`numeric_covid_19_xam_py-title`.
   This reduces the change of a random failure.

.. _whats_new_2020@09-30:

09-30
*****
#. The ``error_message`` routine was replaced by :ref:`exceptions<exception-name>`
   (``error_message`` was not thread safe).
   This is a change to the API, you will have to use exceptions objects
   instead of the ``error_message`` routine to retrieve the error messages.

#. Change the release version so it also throws exceptions for cppad_py error
   messages (cppad error messages still require using the debug version).

.. _whats_new_2020@09-14:

09-14
*****
#. xrst: the target
   command line argument was added and the section numbers were removed
   from the html output. This was done so that adding or removing one
   section does not cause changes in the github pages for all the other
   sections. In addition, the table of contents and link to the index
   now appear in the navigation frame for both the html and pdf output.
   Furthermore, the table of contents uses the section number for the
   link so that the title is easier to read.

#. xrst: A begin_parent must be the first
   begin command in a file. This restriction is new and makes the pdf output
   for the parent come before its children.

.. _whats_new_2020@09-13:

09-13
*****
#. The text ``xrst:`` was added to the beginning of each whats new item
   (see below) that only pertained to the xrst.py program.
#. xrst: The order of the sections in the pdf file and the
   table of contents was corrected.
#. xrst: Put spaces around table of contents levels that have more that one
   entry. Also remove the level of indentation in table of contents by one
   because the root section stands out has having not number in front of it.
#. The latex numbering of sections is incorrect, so change them to the
   corresponding xrst section numbers in both the html and pdf output.
#. xrst: Correct position of sphinx_dir in the
   command line syntax.

.. _whats_new_2020@09-12:

09-12
*****
#. xrst: A table of contents that only contains section titles,
   not headings within a section, was added.
#. xrst: The following restriction was added: a
   section_name
   can not begin with ``xrst_``.

.. _whats_new_2020@07-31:

07-31
*****
#. xrst: An empty line at beginning of xrst input file was causing it to crash
   (this has been fixed).
#. xrst: Putting version number in the documentation navigation side bar
   changes every gh-pages file when version changes. Move it to
   the first heading under the title :ref:`cppad_py-name`
#. xrst: spell checking is not done for a *url* of the form
   \` < *url* > \`_ or \` *text* < *url* > \`_.

.. _whats_new_2020@07-30:

07-30
*****
xrst: The words 'anl', 'dir', 'mcs' were removed from the xrst dictionary.
The word 'initialization' was added to the xrst dictionary.

.. _whats_new_2020@07-29:

07-29
*****
#. xrst: Add the optional command line argument
   line_increment.
   This is an aid for finding the source of errors and warnings
   reported by sphinx.
#. xrst: Sometimes xrst would not recognize a command that came directly after a
   Fix file_cmd. This has been fixed.

.. _whats_new_2020@07-28:

07-28
*****
#. xrst: Move version number from the title in :ref:`cppad_py-name` to
   the documentation navigation side bar.
#. xrst: Add the configure section.
#. xrst: The xrst begin command was not recognized
   at the beginning of a file
   (when there is no new line before it). This has been fixed.
#. xrst: Change the *index_file* to
   keyword
   and *spell_file* to
   spelling

.. _whats_new_2020@07-25:

07-25
*****
#. xrst: Install xrst.py during the
   :ref:`install<setup_py@Install>` procedure.
#. xrst: Add a purpose paragraph to xrst documentation.
#. Move the ``*.omh`` files to ``*.xrst`` files (they have been converted
   from omhelp input files to xrst input files).
#. xrst: Change the keyword
   to use python regular expressions and remove the whats new month-day
   headings from the :ref:`index<genindex>`.

.. _whats_new_2020@07-24:

07-24
*****
#. xrst: Add the xrst.py program
   which extracts sphinx ``*.rst`` files from source code.
   This program is not yet installed but you can use it by placing
   the script ``bin/xrst.py`` in your execution path.
#. Convert the cppad_py documentation to xrst input files,
   which are mostly sphinx rst with a few extra xrst commands.
#. Use xrst and sphinx to generate this documentation for cppad_py.

.. _whats_new_2020@07-18:

07-18
*****

#. The experimental ``bin/xrst.py`` program was added.
   This program runs its tests and builds its documentation
   (in the ``sphinx`` ) directory with the command ``bin/check_xrst.sh``.
   The intention is to convert the cppad_py documentation from omhelp to
   sphinx.
#. Convert all the cppad_py source code to use spaces instead of tabs
   (with tab stops at multiples of 4 spaces).

.. _whats_new_2020@07-05:

07-05
*****

#. The :ref:`prototype<ad_vec_cppad2std@Syntax>` for ``vec2a_double``
   was the same as for :ref:`d_vec_std2cppad<d_vec_cppad2std-name>`.
   This has been fixed.
#. The limits for the :ref:`fun_from_json_xam_py-name` and :ref:`fun_to_json_xam_py-name`
   example code were incorrect (this has been fixed).
#. The in :ref:`fun_from_json_xam_cpp-name` the title was corrected; to be specific,
   to_json was changed to from_json

.. _whats_new_2020@05-17:

05-17
*****
The ``abs`` :ref:`a_double_unary_fun-name` was added
(works the same as the ``fabs`` function).

.. _whats_new_2020@05-16:

05-16
*****

#. A discussion of some subtle issues,
   when interpolation is used to define an ODE,
   was added to the ``ode_multi_step`` ; see
   :ref:`set_t_all_index<numeric_ode_multi_step-name>`.
#. Add the :ref:`alpha<numeric_seirwd_model@p_all@alpha>` parameter to the
   SEIRWD model.

.. _whats_new_2020@05-15:

05-15
*****
The file ``ode_solve.py`` was moved to ``ode_multi_step.py``
and :ref:`numeric_ode_multi_step-name` was extended to allow for different ODE solvers
(steppers).

.. _whats_new_2020@05-14:

05-14
*****

#. The example semi-stiff integrator :ref:`numeric_rosen3_step-name` was added.
#. The example file ``runge4.py`` was moved to ``ode_solve.py``
   in preparation for other solvers.
#. Add the :ref:`numeric_simple_inv-name` example routine for
   AD inversion of matrices.
#. Add mention of which :ref:`numeric_xam-name` routines can take ``a_double`` values.
#. Simplify the :ref:`numeric_seirwd_model_xam_py-name` example using numpy vector operations.
#. More improvements to were made to
   :ref:`covid-19<numeric_covid_19_xam_py-name>` example.

.. _whats_new_2020@05-12:

05-12
*****

#. More improvements to were made to
   :ref:`covid-19<numeric_covid_19_xam_py-name>` example.
#. The :ref:`n_step<numeric_seirwd_model@n_step>` option was added to the
   SEIRWD model example.
#. A delay between when is no longer infectious and when one dies was
   added to the SEIRWD model using a W compartment (Will die compartment).

.. _whats_new_2020@05-09:

05-09
*****
The :ref:`covid-19_modeling_example<numeric_covid_19_xam_py-name>` application
of AD is changing on a regular basis, so the details of the
changes will no longer be tracked in this file, just see current
example if you are interested.

.. _whats_new_2020@05-08:

05-08
*****

#. The ``numeric_seirs_fit_xam.py`` example was renamed
   :ref:`numeric_covid_19_xam_py-name`.
   And it was change to fit covariate multipliers that model
   the infectious rate :math:`\beta`.
#. The ``numeric_seirs_model`` was renamed :ref:`numeric_seirwd_model-name`,
   the D compartment was added to track total deaths,
   the data was changed from Infectious to cumulative death, and
   noise was added to the data.
#. In ``numeric_covid_a9_xam`` ,
   reduce to just E and I as unknowns in initial conditions.
   Initial R = D = 0, S = 1 - E - R.
#. Use the observed information matrix to estimate the covariance
   of the optimal parameters.

.. _whats_new_2020@05-07:

05-07
*****

#. The function ``scipy.misc.factorial``
   has been deprecated so change it to
   ``scipy.special.factorial`` .
#. Add the ``numeric_seirs_model`` utility example
   which allows rates in the ODE to change with time.
   This enabled changing the :ref:`numeric_covid_19_xam_py-name`
   example to estimate a :math:`\beta` coefficient that
   changes with time.
#. The ``numeric_seirs_class`` example was removed because
   ``numeric_seirwd_model`` replaces it with more general
   capabilities.

.. _whats_new_2020@05-06:

05-06
*****

#. Add the following utility examples:
   :ref:`numeric_optimize_fun_class-name`,
   :ref:`numeric_runge4_step-name`,
   :ref:`numeric_ode_multi_step-name`,
   ``numeric_seirs_class`` .
   (The ``numeric_seirs_class`` was later replaced by
   :ref:`numeric_seirwd_model-name`.)
#. Add mention of using ``DYLD_LIBRARY_PATH`` in the
   :ref:`libcppad_lib<install_error@check_all.py@libcppad_lib>`
   install error instructions for the Mac.

.. _whats_new_2020@05-05:

05-05
*****
Add the :ref:`numeric_runge4_step_xam_py-name` example.

.. _whats_new_2020@05-04:

05-04
*****
Add the :ref:`numeric_optimize_fun_xam_py-name` example.

.. _whats_new_2020@04-28:

04-28
*****
The :ref:`f_from_json()<py_fun_json@from_json>` function was added.
In addition, the
:ref:`empty_function<py_fun_ctor@f@Empty Function>` constructor was added.

.. _whats_new_2020@04-27:

04-27
*****
The ``setup.py`` program now installs a separate copy of CppAD
and provides instructions at the end for modifying your
``LD_LIBRARY_PATH``. These instructions have been removed and placed
in the setup.py documentation; see
:ref:`LD_LIBRARY_PATH<setup_py@LD_LIBRARY_PATH>` .

.. _whats_new_2020@04-26:

04-26
*****
The ``setup.py`` program was modified to try to automatically solve the
:ref:`install_error@check_all.py@libcppad_lib` problem.

.. _whats_new_2020@04-25:

04-25
*****
The :ref:`f_to_json()<py_fun_json@to_json>` function was added.

.. _whats_new_2020@04-24:

04-24
*****
The newer Mac systems seems to require that one use
``-stdlib=libc++`` compile and link flag.
The install has been changed to check for and adapt to this condition.
In addition, :ref:`setup_py-name` now runs the ``cmake`` command; i.e.,
the user no longer needs to run ``cmake`` to test the C++ library.

.. _whats_new_2020@04-23:

04-23
*****
Add an :ref:`install_error-name` section to the documentation.

.. _whats_new_2020@04-22:

04-22
*****

#. Instructions were added for installing using pip
   (this install was not kept up to date and has been removed).
#. The binary operators were extended to include *x* ``op`` *ay* where:
   *x* is a double (python ``float`` ),
   *ay* is an ``a_double`` ,
   and *op* is
   ``+`` ,
   ``-`` ,
   ``*`` ,
   ``/`` , or
   ``**`` .
   Note that this automatically transfers to numpy arrays; e.g
   *x* ``*`` *ay* where *x* is a double and *ay*
   is a numpy array of ``a_double`` .

.. _whats_new_2020@04-20:

04-20
*****

#. Move configuration setting from :ref:`setup_py-name` to
   :ref:`bin/get_cppad_sh<get_cppad_sh@Settings>`.
#. First version that installs using ``pip`` .
   Install instructions for pip will be added soon.

.. _whats_new_2020@04-19:

04-19
*****

#. Move the python source that gets distributed from ``lib/python``
   to ``lib/python/cppad_py`` so that more like a standard python package.
#. Drop support for python2. It is not consistent with python3 in
   some of the ``setup.py`` actions.

.. _whats_new_2020@04-18:

04-18
*****

#. Change *yq* to *xq* , correct documentation,
   for *xq* in the
   :ref:`c++<cpp_fun_reverse@xq>` and :ref:`python<py_fun_reverse@xq>`
   reverse mode documentation.
#. Remove the ``--inplace`` option from the
   :ref:`syntax<setup_py@Syntax>` for building the cppad_py python module.

.. _whats_new_2020@04-13:

04-13
*****

#. The *z* =  ``pow`` ( *x* , *y* ) functions was added; see
   :ref:`a_double_binary-name`.
#. Add the :ref:`var2par<a_double_property@var2par>` function
   and improve the notation in the
   :ref:`near_equal<a_double_property@near_equal>` notation.

.. _whats_new_2020@04-12:

04-12
*****

#. Add the ``erf`` function was added to the
   list of ``a_double`` unary :ref:`fun<a_double_unary_fun@fun>`
   that have been implemented.
#. The dynamic parameter argument was missing from the
   :ref:`syntax<py_independent@Syntax>` for the python version
   of the ``independent`` function.  This has been fixed.
#. Improve the test and :ref:`install<setup_py@Install>`
   discussion in ``setup.py`` .

.. _whats_new_2020@04-10:

04-10
*****

#. Change the documentation display on the web using a more recent version of
   the documentation program ``omhelp-20200130`` .
#. Add :ref:`caching<get_cppad_sh@Caching>` to the Cppad install.
