"""
********************************************************************************
compas_rcf.rhino
********************************************************************************

.. currentmodule:: compas_rcf.rhino

Rhino package installer
=======================
``compas_rcf.rhino.install`` installs
`compas <https://compas-dev.github.io/>`_,
`compas_fab <https://gramaziokohler.github.io/compas_fab>`_,
`roslibpy <https://roslibpy.readthedocs.io/>`_,
`compas_rrc <https://bitbucket.org/ethrfl/compas_rrc/>`_ and ``compas_rcf`` to
Rhino's IronPython lib directory using the ``compas_rhino`` installer.

Usage: ``python -m compas_rcf.rhino.install``

RhinoCommon to COMPAS object conversions and other utilities
============================================================
Scripts for converting geometry objects between the two frameworks. Most of this
has been integrated into COMPAS v0.15.0 but compas_fab needs earlier versions
of COMPAS.

Points
------

.. autosummary::
   :toctree: generated/

   cgpoint_to_rgpoint
   rgpoint_to_cgpoint

Vectors
-------

.. autosummary::
   :toctree: generated/

   cgvector_to_rgvector
   rgvector_to_cgvector

Lines
-----

.. autosummary::
   :toctree: generated/

   cgline_to_rgline
   rgline_to_cgline

Planes & Frames
---------------

.. autosummary::
   :toctree: generated/

   cgplane_to_rgplane
   rgplane_to_cgplane
   rgplane_to_cgframe

Transformations
---------------

.. autosummary::
   :toctree: generated/

   matrix_to_rgtransform
   rgtransform_to_matrix
"""
from .compas_to_rhino import *  # noqa: F401,F403
from .rhino_to_compas import *  # noqa: F401,F403
