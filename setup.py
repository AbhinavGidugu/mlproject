from setuptools import find_packages,setup
from typing import List

setup_initiator="-e."
def get_requirements(file:str)->List[str]:
    #returns list of requirements
    requirements=[]
    with open(file) as file_obj:
        requirements=file_obj.readlines()
        requirements=[req.replace("\n","") for req in requirements]
    if setup_initiator in requirements:
        requirements.remove(setup_initiator)
    
    return requirements

setup(
name="MLproject",
version="0.0.1",
author="Abhinav Gidugu",
author_email="abhinavgidugu2495@gmail.com",
packages=find_packages(),
requires=get_requirements("requirements.txt")
)