# cppad\_py: A Python Interface To CppAD

## Documentation
https://bradbell.github.io/cppad_py

## Description
cppad\_py contains the following:

- Python AD package (Algorithmic or Automatic Differentiation).
- Python mixed effects Laplace Approximation optimizer.
- Python interface to Ipopt.
- C++ library that can connect AD to other scripting languages.

## Simple Example
```python
import numpy
import cppad_py
x    = numpy.array( [ 1, 2], dtype = float)
ax   = cppad_py.independent(x)
ay   = ax * ax
f    = cppad_py.d_fun(ax, ay)
x[0] = 2.0
x[1] = 3.0
y    = f.forward(0, x)
assert all( y == x * x )
J    = f.jacobian(x)
assert J.shape == (2,2)
assert J[0,0] == 2.0 * x[0]
assert J[0,1] == 0.0
assert J[1,0] == 0.0
assert J[1,1] == 2.0 * x[1]
```

## Install
[setup.py](https://bradbell.github.io/cppad_py/cppad_py.xrst/setup_py.html)

### Error
If you get a warning or error message during the install process; see
[install error](https://bradbell.github.io/cppad_py/cppad_py.xrst/install_error.html)

## License
<pre>
SPDX-License-Identifier: GPL-3.0-or-later
SPDX-FileCopyrightText: Bradley M. Bell <bradbell@seanet.com>
SPDX-FileContributor: 2017-22 Bradley M. Bell
</pre>
