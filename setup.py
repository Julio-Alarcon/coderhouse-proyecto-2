import os
from setuptools import setup, find_packages

setup(
    name = "paquete_proyecto_2",
    version = "1.6",
    description = "Paquete distribuido para el proyecto de CoderHouse",
    author = "Julio Alarcon Caballero",
    author_email = "julio.alarconca@gmail.com",
    packages = find_packages(exclude=['test']),
)
