import sys
#from distutils.core import setup
from setuptools import setup, find_packages

long_description = \
"""
    ACOLITE allows simple and fast processing of imagery from various satellites, 
    including Landsat (5/7/8) and Sentinel-2/MSI (A/B), PlanetScope and RapidEye, 
    Venµs, SPOT and Pléiades, WorldView-2 and -3, and Sentinel-3/OLCI (A/B) for 
    coastal and inland water applications. The Dark Spectrum Fitting atmospheric 
    correction algorithm works especially well for turbid and productive waters, 
    but can also be applied over clear waters and land with reasonable success.
""" 

setup(
    name="acolite"
    , description=long_description
    , long_description=long_description     
    , author="Quinten Vanhellemont"
    , author_email='qvanhellemont@naturalsciences.be'
    , url='https://github.com/acolite/acolite'
    , download_url = 'https://github.com/jtwhite79/pyemu/tarball/1.1.0'
    , license='?'
    , platforms='Windows, Mac OS-X, Linux'
    , version="20210802.0"
    , packages = find_packages(where='acolite')
)
