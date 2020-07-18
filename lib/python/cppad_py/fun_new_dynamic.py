# -----------------------------------------------------------------------------
#         cppad_py: A C++ Object Library and Python Interface to Cppad
#          Copyright (C) 2017-20 Bradley M. Bell (bradbell@seanet.com)
#              This program is distributed under the terms of the
#              GNU General Public License version 3.0 or later see
#                    https://www.gnu.org/licenses/gpl-3.0.txt
# -----------------------------------------------------------------------------
# $begin py_fun_new_dynamic$$ $newlinech #$$
# $spell
#   numpy
# $$
#
# $section New Dynamic Parameters$$
#
# $head Syntax$$
# $icode%f%.new_dynamic(%dynamic%)%$$
#
# $head f$$
# This is either a
# $cref/d_fun/py_fun_ctor/Syntax/d_fun/$$ or
# $cref/a_fun/py_fun_ctor/Syntax/a_fun/$$.
# The independent $cref/dynamic/py_independent/dynamic/$$ parameters
# are changed to have the specified values.
# The other dynamic parameters are then computed.
#
# $head dynamic$$
# If $icode f$$ is a $code d_fun$$ ($code a_fun$$) object,
# $icode dynamic$$ is a numpy vector with $code float$$ ($code a_double$$)
# elements and its size must be the same as the size of
# $cref/dynamic/py_independent/dynamic/$$ in the corresponding call to
# $code independent$$.
# It specifies new values for the dynamic parameters in $icode f$$.
#
# $subhead size_order$$
# After this call,
# $cref/f.size_order()/py_fun_property/size_order/$$ is zero.
#
# $head Example$$
# See $cref fun_dynamic_xam.py$$
#
# $end
# -----------------------------------------------------------------------------
import cppad_py
import numpy
# ----------------------------------------------------------------------------
# This function is used by d_fun class to implement syntax above
def d_fun_new_dynamic(f, dynamic) :
    """
    f.new_dynamic(dynamic)
    Set the independent dynamic parameters and compute the others.
    """
    #
    # convert x -> u
    dtype    = float
    syntax   = 'f.dynamic(p, dynamic)'
    n        = dynamic.size
    u        = cppad_py.utility.numpy2vec(dynamic, dtype, n, syntax, 'xp')
    f.new_dynamic(u)
# ----------------------------------------------------------------------------
# This function is used by a_fun class to implement syntax above
def a_fun_new_dynamic(af, adynamic) :
    """
    af.new_dynamic(adynamic)
    Set the independent dynamic parameters and compute the others.
    """
    #
    # convert x -> u
    dtype    = cppad_py.a_double
    syntax   = 'af.dynamic(adynamic)'
    n        = adynamic.size
    au       = cppad_py.utility.numpy2vec(adynamic, dtype, n, syntax, 'dynamic')
    af.new_dynamic(au)
