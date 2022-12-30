#! /usr/bin/env python3
# SPDX-License-Identifier: GPL-3.0-or-later
# SPDX-FileCopyrightText: Bradley M. Bell <bradbell@seanet.com>
# SPDX-FileContributor: 2017-22 Bradley M. Bell
# ----------------------------------------------------------------------------
# prints the standard library directory for site packages; e.g., lib or lib64
import sysconfig
stdlib = sysconfig.get_paths()['stdlib']
stdlib = stdlib.split('/')
assert 2 <= len( stdlib )
assert stdlib[-1].startswith( 'python' )
print( stdlib[-2], end='' )
