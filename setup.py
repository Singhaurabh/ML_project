from setuptools import find_packages, setup
from typing import List

HYPER_E_DOT= '-e .'
def get_requirements(file_path:str)->List[str]:
    requirements = []
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        requirements=[req.replace('\n',"")for req in requirements]    

        if HYPER_E_DOT in requirements:
            requirements.remove(HYPER_E_DOT)

        return requirements


setup(
    # these are the meta data of project
    name= 'ml_project',
    version = '0.1',
    packages = find_packages(),
    include_package_data = True,
    author = "Saurabh Singh",
    author_email = "ss1477889@gmail.com",
    install_requires = get_requirements('requirements.txt'),

)