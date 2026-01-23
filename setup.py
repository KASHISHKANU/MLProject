from setuptools import setup,find_packages
from typing import List
HYFEN_E_DOT = "-e ."

def get_requirements(file_path:str)->List[str]:
    """This function will return the list of requirements"""
    with open(file_path) as file:
        requirements = file.readlines()
        requirements = [req.replace("\n","") for req in requirements]

        if HYFEN_E_DOT in requirements:
            requirements.remove(HYFEN_E_DOT)
    return requirements
# Metadata of the project 
setup(
    name="MyProject",# name of the project
    version="0.1.0",# version of the project
    author="Kashish",# author of the project,
    author_email="lunakanu085@gmail.com",# email of the author,
    packages=find_packages(),# packages to be included in the project
    install_requires=get_requirements("requirements.txt")# dependencies of the project
)