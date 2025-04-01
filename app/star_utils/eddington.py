'''
Eddington Ratio Calculations

This module provides functions to calculate the Eddington luminosity and Eddington ratio.
The Eddington ratio is a measure of the balance between radiation pressure and gravitational force on a massive object, such as a black hole or neutron star.
'''
import numpy as np

G = 6.67430e-8       # Gravitational constant (cm^3 g^-1 s^-2)
c = 2.99792458e10    # speed of light (cm/s)
m_p = 1.6726219e-24  # mass of a proton (g)
sigma_T = 6.6524587e-25  # Thompson scattering cross-section (cm^2)

def calculate_eddington_luminosity(mass_solar: float) -> float:
    """
    Calculate the Eddington luminosity for a given mass.

    args:
        mass_solar: Mass in solar masses.

    returns:
        Eddington luminosity in erg/s.
    """
    mass_grams = mass_solar * 1.989e33  # Convert solar masses to grams
    return (4 * np.pi * G * mass_grams * m_p * c) / sigma_T

def calculate_eddington_ratio(luminosity: float, mass_solar: float) -> float:
    """
    Calculate the Eddington ratio for a given luminosity and mass.

    args:
        luminosity: Luminosity in erg/s.
        mass_solar: Mass in solar masses.

    returns:
        Eddington ratio.
    """
    L_edd = calculate_eddington_luminosity(mass_solar)
    return luminosity / L_edd