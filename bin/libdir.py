#! /usr/bin/env python3
# -----------------------------------------------------------------------------
#         cppad_py: A C++ Object Library and Python Interface to Cppad
#          Copyright (C) 2017-20 Bradley M. Bell (bradbell@seanet.com)
#              This program is distributed under the terms of the
#              GNU General Public License version 3.0 or later see
#                    https://www.gnu.org/licenses/gpl-3.0.txt
# -----------------------------------------------------------------------------
# prints the standard library directory for site packages; e.g., lib or lib64
import sysconfig
stdlib = sysconfig.get_paths()['stdlib']
stdlib = stdlib.split('/')
assert 2 <= len( stdlib )
assert stdlib[-1].startswith( 'python' )
print( stdlib[-2], end='' )
