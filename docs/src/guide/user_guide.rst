Getting Started
===============

This package leverages a parallelization boiler-plate code to provide a super fast source finder routine which deletes background sources using a polygon based approach.

Watch the video on `YouTube video <https://www.youtube.com/watch?v=cO5TYy396xU>`_ for detailed instructions on how to use the data analysis scripts. Hopefully, it will not put you to sleep! More detailed written instructions may follow.

Main scripts
------------
There are two main scripts in the package, viz: `get_morphology_images` and `get_galaxy_parameters`.

get_morphology_images
*********************

Uses morphological erosion and dilation to remove background sources from a radio astronomy image. It extends the technique described in `Rudnick, 2002 <https://iopscience.iop.org/article/10.1086/342499/pdf>`_.

The process can be described through the following equations:

.. TODO find a better way to have the equations under one directive

.. math:: t = o - d
.. math:: m * t = m * (o - d)
.. math:: =o - m * t
.. math:: =o - (m * o - m * d)
.. math:: =o - m * o + (m * d)


.. code-block:: console

   o = original image
   d = output from erosion/dilation
   t = white TopHat, which should show only 'compact' structures
   m = mask derived from a comparison where t > some signal

:math:`m*d` would add the masked dilated image to the 'diffuse' image and we do not want to do that so we ignore it to get
:math:`o_d` = output diffuse image and :math:`o_c` = image of compact objects.

:math:`o_d = o - m * o`

:math:`o_c = m * o`

So the original image equates to :math:`o_d + o_c`. We may want to judiciously add selected components of :math:`o_c` to :math:`o_d`
to get a final :math:`o*`. We select the components of :math:`o_c` we wish to add by masking their defining polygons to get a mask :math:`m_c`

.. math:: 

   o* = o_d + m_c * o_c

get_galaxy_parameters
*********************

Integrates the signal contained within specified polygon areas of a radio astronomy image to derive integrated flux densities and other parameters of a radio source.


Requirements
------------

The code has been tested with python 3.8 on Ubuntu 20.04. See ``pyproject.toml`` or ``requirements.txt`` for package dependencies.

Installation
------------

Install from source

.. code-block:: bash

   > pip install .


Use the routine

.. code-block:: bash

   > tw-source-list -f xyz.fits -t 6.5
