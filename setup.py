from setuptools import setup, find_packages
import setuptools
import os
import sys

base_dir = os.path.dirname(__file__)
src_dir = os.path.join(base_dir, 'src')
sys.path.insert(0, src_dir)

def get_requirements(requirements_path='requirements.txt'):
    with open(requirements_path) as fp:
        return [x.strip() for x in fp.read().split('\n') if not x.startswith('#')]

setuptools.setup(
    name='cruasan',
    version='0.1',
    description='Library for CDS HW5',
    license = 'MIT',
    author='Catalina Odizzio, Agostina Pissinis, Santiago Manotas-Arroyave',
    packages=find_packages(where='src', exclude=['tests']),
    package_dir={'': 'src'},
    install_requires=get_requirements(),
    setup_requires=['pytest-runner', 'wheel'],
    url='',
    classifiers=[
        'Programming Language :: Python :: 3.9.12'
    ]
)