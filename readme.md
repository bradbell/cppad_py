# cppad\_py: A Python Interface To CppAD

## Documentation
https://cppad-py.readthedocs.io

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
[setup.py](https://cppad-py.readthedocs.io/en/latest/setup_py.html)

### Error
If you get a warning or error message during the install process; see
[install error](https://cppad-py.readthedocs.io/en/latest/install_error.html)
