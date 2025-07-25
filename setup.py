from setuptools import setup, find_packages

with open('requirements.txt') as f:
    requirements = f.read().splitlines()

setup(
    name = "Hotel_Reservation_MLOPS",
    version = "0.1",
    author = "Sandeep Hidellarachchi",
    author_email = "sandeeprox96@gmail.com",
    packages = find_packages(),
    install_requires = requirements
)