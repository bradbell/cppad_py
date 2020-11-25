#! /bin/bash -e
# -----------------------------------------------------------------------------
#         cppad_py: A C++ Object Library and Python Interface to Cppad
#          Copyright (C) 2017-20 Bradley M. Bell (bradbell@seanet.com)
#              This program is distributed under the terms of the
#              GNU General Public License version 3.0 or later see
#                    https://www.gnu.org/licenses/gpl-3.0.txt
# -----------------------------------------------------------------------------
# Test all possible settings for build_type and include_mixed
if [ "$0" != "bin/double_check.sh" ]
then
    echo "bin/double_check.sh: must be executed from its parent directory"
    exit_code 1
fi
# -----------------------------------------------------------------------------
# cmake_install_prefix
cmd=`grep '^cmake_install_prefix=' bin/get_cppad.sh`
eval $cmd
# -----------------------------------------------------------------------------
# Clean out old results
if [ -e $HOME/prefix/$cmake_install_prefix ]
then
    rm $HOME/prefix/$cmake_install_prefix
fi
for ext in debug release
do
    if [ -e $HOME/prefix/$cmake_install_prefix.$ext ]
    then
        rm -r $HOME/prefix/$cmake_install_prefix.$ext
    fi
done
if [ -e double_check.log ]
then
    rm double_check.log
fi
# -----------------------------------------------------------------------------
for include_mixed in false true
do
    for build_type in debug release
    do
        printf '%79s\n' '' | tr ' ' '-' >> double_check.log
        printf 'build_type = %s\n'    $build_type >> double_check.log
        printf 'include_mixed = %s\n' $include_mixed >> double_check.log
        #
        # change bin/get_cppad.sh to requested configuration
        sed -i.bak \
            -e "s|^build_type=.*|build_type='$build_type'|" \
            -e "s|^include_mixed=.*|include_mixed='$include_mixed'|" \
            bin/get_cppad.sh
        rm bin/get_cppad.sh.bak
        #
        # get external requirements
        if [ "$include_mixed" == 'true' ]
        then
            echo 'bin/get_cppad_mixed.sh >> double_check.log'
            bin/get_cppad_mixed.sh >> double_check.log
        else
            echo 'bin/get_cppad.sh >> double_check.log'
            bin/get_cppad.sh >> double_check.log
        fi
        # change bin/get_cppad.sh back to standard configuration
        sed -i.bak \
            -e "s|^build_type=.*|build_type='release'|" \
            -e "s|^include_mixed=.*|include_mixed='false'|" \
            bin/get_cppad.sh
        rm bin/get_cppad.sh.bak
        #
        # run test for this configuration
        bin/check_all.sh $build_type $include_mixed
        #
        # double_check.log
        cat check_all.log >> double_check.log
    done
done
# -----------------------------------------------------------------------------
echo 'double_check.sh: OK'
exit 0
