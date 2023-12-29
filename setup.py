from setuptools import find_packages,setup
from typing import List

def get_requirements(file_path:str)->List[str]:
    requrirements=[]
    with open(file_path) as file_obj:
        requrirements=file_obj.readlines()
        requrirements=[req.replace("\n","")for req in requrirements]
        return requrirements


setup(
  name='DiamondPricePrediction',
  version='0.0.1',
  author='chirag',
  author_email='chikisola@pw.live',
  install_requires=get_requirements('requirements.txt'),
  packages=find_packages()




)