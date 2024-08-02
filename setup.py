from setuptools import find_packages, setup
from typing import List

def get_requirements(file_path:str)->List[str]:
    requirements = []
    with open(file_path) as file_obj:
        requirements = file_obj.readlines() #read everylines
        requirements = [req.replace("\n","") for req in requirements] # relapce with new line's characters

        return requirements

setup(
    name = 'DiamondPricePrediction',
    version='0.0.1',
    author = 'Rohit Jana',
    author_email= 'jdipankar34@gmail.com',
    install_requires=get_requirements('requirements.txt')
)