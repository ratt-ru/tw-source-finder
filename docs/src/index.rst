================
tw-source-finder
================

Description
===========

A super-fast (leveraging a boiler-plate parallelization) source finder routine
using polygon based approach for deleting background sources. Using the inner
quarter of the ASKAP first pilot survey image (20K x 20K in size) the finder can
detect 165K sources in 130 seconds wall-clock time on a 32GB memory laptop. The
basic trick is to realize that the actual image is 'read-only' so it can be shared
between all parallel processes as a global object.

Check out `YouTube video <https://www.youtube.com/watch?v=cO5TYy396xU>`_ to see it in use.

.. README =============================================================

.. This project most likely has it's own README. We include it here.

.. toctree::
   :maxdepth: 1
   :caption: README

   guide/readme


Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
