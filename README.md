# cppad\_py: A Python Interface To CppAD

## Documentation
<https://bradbell.github.io/cppad_py/doc>

## Description
cppad\_py contains the following:

- A Python AD package (Algorithmic or Automatic Differentiation).
- A Python mixed effects Laplace Approximation optimizer.
- A C++ library that can be used to connect other scripting languages to AD

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

## Covid-19
A Covid-19 model, that is currently being improved,
is included as an example; see
[covid_19_xam](https://bradbell.github.io/cppad_py/doc/xsrst/numeric_covid_19_xam_py.html?highlight=covid%2019)

## Install
[setup.py](https://bradbell.github.io/cppad_py/doc/xsrst/setup_py.html)

### Error
If you get a warning or error message during the install process; see
[install error](https://bradbell.github.io/cppad_py/doc/xsrst/install_error.html)

## License
<pre>
Copyright (C) 2017-20 Bradley M. Bell (bradbell@seanet.com)
    This program is distributed under the terms of the
    GNU General Public License version 3.0 or later see
        https://www.gnu.org/licenses/gpl-3.0.txt
</pre>
