import os
from setuptools import setup, find_packages

f = open(os.path.join(os.path.dirname(__file__), 'README.rst'))
readme = f.read()
f.close()

setup(
    name='fancy_tag',
    version='0.1.2', 
    description="A replacement for Django's simple_tag decorator.",
    long_description=readme,
    author='tamask',
    url='https://github.com/trapeze/fancy_tag',
    packages=find_packages(),
    zip_safe=False,
    classifiers=[
        'Programming Language :: Python',
        'Framework :: Django',
    ],
)

