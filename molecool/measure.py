"""
Functions for performing measurement
"""

import numpy as np

from .atom_data import atomic_weights


def calculate_distance(rA, rB):
    """
    Caculate the distance between two points

    Parameters
    ----------
    rA, rB : np.ndarray
        The coordinate of each points.

    Returns
    -------
    dist : float
        The distance between the two points

    Examples
    --------
    >>> r1 = np.array([0, 0, 0])
    >>> r2 = np.array([0, 0.1, 0])
    >>> calculate_distance(r1, r2)
    0.1
    """

    d = rA - rB
    dist = np.linalg.norm(d)
    return dist


def calculate_angle(rA, rB, rC, degrees=False):
    # Calculate the angle between three points. Answer is given in radians by default, but can be given in degrees
    # by setting degrees=True
    AB = rB - rA
    BC = rB - rC
    theta = np.arccos(np.dot(AB, BC) / (np.linalg.norm(AB) * np.linalg.norm(BC)))

    if degrees:
        return np.degrees(theta)
    else:
        return theta


def calculate_molecular_mass(symbols):
    """
    Calculate the mass of a molecule.

    Parameters
    ----------
    symbols : list
        A list of elements.

    Returns
    -------
    mass : float
        The mass of the molecule
    """

    mass = 0

    for symbol in symbols:
        mass += atomic_weights[symbol]

    return mass


def calculate_center_of_mass(symbols, coordinates):
    """Calculate the center of mass of a molecule.

    The center of mass is weighted by each atom's weight.

    Parameters
    ----------
    symbols : list
        A list of elements for the molecule
    coordinates : np.ndarray
        The coordinates of the molecule.

    Returns
    -------
    center_of_mass: np.ndarray
        The center of mass of the molecule.

    Notes
    -----
    The center of mass is calculated with the formula

    .. math:: \\vec{R}=\\frac{1}{M} \\sum_{i=1}^{n} m_{i}\\vec{r_{}i}

    """
    total_mass = calculate_molecular_mass(symbols)
    mass_arr = np.zeros([len(symbols), 1])

    for i in range(len(symbols)):
        mass_arr[i] = atomic_weights[symbols[i]]

    center_of_mass = sum(coordinates * mass_arr) / total_mass
    return center_of_mass
