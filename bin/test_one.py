#! /usr/bin/env python3
# SPDX-License-Identifier: GPL-3.0-or-later
# SPDX-FileCopyrightText: Bradley M. Bell <bradbell@seanet.com>
# SPDX-FileContributor: 2017-22 Bradley M. Bell
# ----------------------------------------------------------------------------
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
dir_list= [
   'test/mixed',
   'example/python/core',
   'example/python/numeric',
   'example/python/mixed',
]
for local_dir in dir_list :
   if os.path.isfile( local_dir + '/' + name_py ) :
      if found_dir is None :
         found_dir = local_dir
      else :
         msg  = 'bin/test_one.sh: found two version of ' + name_py
         msg += local_dir + '/' + name_py + '\n'
         msg += found_dir + '/' + name_py
         sys.exit(msg)
if found_dir is None :
   msg  = 'could not find ' + name_py
   msg += ' below example/python or test/python'
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
