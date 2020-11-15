#! /usr/bin/env python3
# -----------------------------------------------------------------------------
#         cppad_py: A C++ Object Library and Python Interface to Cppad
#          Copyright (C) 2017-20 Bradley M. Bell (bradbell@seanet.com)
#              This program is distributed under the terms of the
#              GNU General Public License version 3.0 or later see
#                    https://www.gnu.org/licenses/gpl-3.0.txt
# -----------------------------------------------------------------------------
# Run on python test
import sys
import os
# ---------------------------------------------------------------------------
if sys.argv[0] != 'bin/test_one.py' :
    msg = 'bin/test_one.py: must be executed frorm its parent directory'
    sys.exit(msg)
if len(sys.argv) != 2 :
    msg  = 'bin/test_one.sh name\n'
    sys.exit(msg)
name      = sys.argv[1]
name_py   = name + '.py'
# ---------------------------------------------------------------------------
found_dir = None
for local_dir in [ 'core', 'numeric', 'mixed' ] :
    sub_dir = 'example/python/' + local_dir
    if os.path.isfile( sub_dir + '/' + name_py ) :
        if found_dir is None :
            found_dir = sub_dir
        else :
            msg  = 'bin/test_one.sh: found two version of ' + name_py
            msg += sub_dir + '/' + name_py + '\n'
            msg += found_dir + '/' + name_py
            sys.exit(msg)
if found_dir is None :
    msg = 'could not find ' + name_py + ' below example/python'
    sys.exit(msg)
# ---------------------------------------------------------------------------
def run_test(module_name, fun_name) :
    namespace = {} # not needed in Python 2
    exec( 'import ' + module_name,                         namespace )
    exec( 'ok = '   + module_name + '.' + fun_name + '()', namespace )
    ok = namespace['ok']
    if ok :
        print('python: ' + name + ': OK')
    else :
        print('python: ' + name + ': Error')
    return ok
# ---------------------------------------------------------------------------
top_srcdir = os.getcwd()
sys.path.insert(0, top_srcdir)
sys.path.insert(0, '.')
os.chdir(found_dir)
ok = run_test(name, name)
if ok :
    print('bin/test_one.py: OK')
    sys.exit(0)
sys.exit('bin/test_one.py: Error')
