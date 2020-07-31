#! /bin/bash -e
# -----------------------------------------------------------------------------
#         cppad_py: A C++ Object Library and Python Interface to Cppad
#          Copyright (C) 2017-20 Bradley M. Bell (bradbell@seanet.com)
#              This program is distributed under the terms of the
#              GNU General Public License version 3.0 or later see
#                    https://www.gnu.org/licenses/gpl-3.0.txt
# -----------------------------------------------------------------------------
# bash function that echos and executes a command
echo_eval() {
    echo $*
    eval $*
}
# -----------------------------------------------------------------------------
if [ "$0" != "bin/run_xsrst.sh" ]
then
    echo "bin/run_xsrst.sh: must be executed from its parent directory"
    exit 1
fi
project='cppad_py'
if ! grep "{xsrst_begin $project}" doc.xsrst > /dev/null
then
    echo "can not find {xsrst_begin $project} in doc.xsrst"
    exit 1
fi
# -----------------------------------------------------------------------------
echo_eval bin/xsrst.py doc.xsrst sphinx spelling keyword
echo_eval cd sphinx
echo_eval make html
cat << EOF > _build/index.html
<html><head><script>
    window.location.href="html/xsrst/$project.html";
</script></head></html>
EOF
# -----------------------------------------------
echo 'run_xsrst.sh: OK'
exit 0
