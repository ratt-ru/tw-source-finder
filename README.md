tw-source-finder
================

[![Documentation Status](https://readthedocs.org/projects/tw-source-finder/badge/?version=latest)](https://tw-source-finder.readthedocs.io/en/latest/?badge=latest)

This package leverages a parallelization boiler-plate code to provide a super fast source finder routine which deletes background sources using a polygon based approach.

Watch the video on [YouTube](https://www.youtube.com/watch?v=cO5TYy396xU) for detailed instructions on how to use the data analysis scripts. Hopefully, it will not put you to sleep! More detailed written instructions may follow.

Features
--------
There are two main scripts in the package, viz: `get_morphology_images` and `get_galaxy_parameters`.

**get_morphology_images**

Uses morphological erosion and dilation to remove background sources from a radio astronomy image. It extends the technique described in [Rudnick, 2002](https://iopscience.iop.org/article/10.1086/342499/pdf).

The process can be described through the following equations:

```
o = original image

d = output from erosion/dilation

t = white TopHat, which should show only 'compact' structures

t = o - d

m = mask derived from a comparison where t > some signal m * t = m * (o - d)

o_d = output diffuse image

=o - m * t

=o - (m * o - m * d)

=o - m * o + (m * d)

m*d would add the masked dilated image to the 'diffuse' image and we do not want to do that so we ignore it to get

o_d = o - m * o and

o_c = image of compact objects = m * o

so the original image equates to o_d + o_c
```

We may want to judiciously add selected components of `o_c` to `o_d` to get a final `o*`. We select the components of `o_c` we wish to add by masking their defining polygons to get a mask `m_c`

$$o* = o_d + m_c * o_c$$

**get_galaxy_parameters**

Integrates the signal contained within specified polygon areas of a radio astronomy image to derive integrated flux densities and other parameters of a radio source.


Requirements
------------

The code has been tested with python 3.8 on Ubuntu 20.04. See `pyproject.toml` or `requirements.txt` for package dependencies.

Installation
------------

Install from source

```bash
$ pip install .
```

Use the routine

```bash
$ tw-source-list -f xyz.fits -t 6.5
```
