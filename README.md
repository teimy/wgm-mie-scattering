
# Summary of wgm-mie-scattering
This Python package is allows you to compute the scattering properties
of airborne spherical particles. This is useful for remote sensing of
clouds (and aerosols) in the atmosphere. Mie calculations are in FORTRAN
codes written by Michael Mishchenko. This package allows you to run 
Michael's calculations from Python. Original repo and wrapping done by Will Martin.

The output is given as an array of generalized spherical function
coefficients (scaled by the extinction), but the output arrays have a method
called `angle_eval` which returns the scattering matrix at specified
angles. 

## Requirements
- Python with `numpy`, `scipy`, `f2py` (i.e. `anaconda` package)
- `gfortran`: `sudo apt-get install gfortran`/`brew install gcc`
- `meson` and `ninja` for `f2py`: `conda install meson ninja`

## System-wide install

Check out this repository:
```
git clone https://github.com/teimy/wgm-mie-scattering
```

Change to the repository directory and build FORTRAN source code
```
cd wgm-mie-scattering
pip install . --no-build-isolation
```

## References
Fortran source code thanks to Michael Mishchenko: 
http://www.giss.nasa.gov/staff/mmishchenko/

Python wrapping thanks to Will Martin:
https://github.com/wgm2111/wgm-mie-scattering

