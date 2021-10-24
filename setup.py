import os
#from distutils.core import setup
from setuptools import setup
import subprocess

setup(name='seco',
    install_requires=[        
        'sbol3',
    'tyto'
        ],
    setup_requires=[
        'sbol3',
    'tyto' 
        ],
    packages=['seco'],
    python_requires='>=3',
    version='v0.0'
)
