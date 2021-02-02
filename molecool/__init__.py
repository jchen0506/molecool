"""
molecool
A python package for analyzing and visualizing molecular files. For MolSSI workshop.
"""

# Add imports here
from .functions import *
from .measure import calculate_angle, calculate_center_of_mass, calculate_distance, calculate_molecular_mass
from .io import open_pdb, open_xyz, write_xyz
from .visualize import bond_histogram, draw_molecule
from .molecule import build_bond_list

# Handle versioneer
from ._version import get_versions
versions = get_versions()
__version__ = versions['version']
__git_revision__ = versions['full-revisionid']
del get_versions, versions
