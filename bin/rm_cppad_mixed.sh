#! /usr/bin/env bash
# SPDX-License-Identifier: GPL-3.0-or-later
# SPDX-FileCopyrightText: Bradley M. Bell <bradbell@seanet.com>
# SPDX-FileContributor: 2017-23 Bradley M. Bell
# ----------------------------------------------------------------------------
#
# {xrst_begin rm_cppad_mixed.sh}
# {xrst_spell
#     uninstall
#     cppad
#     rm
# }
# {xrst_comment_ch #}
#
# Uninstall get_cppad_mixed.sh
# ############################
#
# Syntax
# ******
# | |tab| ``bin/rm_cppad_mixed.sh``
#
# Purpose
# *******
# This will remove any files that were installed by
# :ref:`get_cppad_mixed_sh-name` .
# This assumes that the values of
# :ref:`get_cppad_sh@Settings@cmake_install_prefix` and
# :ref:`get_cppad_sh@Settings@build_type` have not changed.
#
# {xrst_end rm_cppad_mixed.sh}
# ----------------------------------------------------------------------------
set -e -u
#
cd 'external/cppad_mixed.git'
bin/example_remove.sh
#
echo 'rm_cppad_mixed.sh: OK'
exit 0
