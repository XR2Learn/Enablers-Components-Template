from setuptools import setup

setup(
    name='{{ cookiecutter.project_slug }}',
    version='0.1.0',
    description='{{ cookiecutter.description }}',
    author='UM-XR2Learn-Enablers',
    packages=['{{ cookiecutter.project_slug }}'],
    zip_safe=False
)
