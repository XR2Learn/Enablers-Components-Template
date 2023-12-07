from setuptools import setup

setup(
    name='{{ cookiecutter.project_slug }}',
    version='{{ cookiecutter.current_version }}',
    description='{{ cookiecutter.description }}',
    author='UM-XR2Learn-Enablers',
    packages=['{{ cookiecutter.project_slug }}'],
    zip_safe=False
)
