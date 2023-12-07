![XR2Learn](https://raw.githubusercontent.com/XR2Learn/.github/5c0fada6136915b389c1cd2151a0dd2cfc4a5aac/images/XR2Learn%20logo.png)

# Enablers' Components CookieCutter Template

Project to support creating new components for Enablers 2-6 to extend supported modalities, e.g., preprocessing for BM modality.

## Installing Cookiecutter

`$ pip install --user cookiecutter`,

ref: [cookiecutter installation page](https://cookiecutter.readthedocs.io/en/latest/installation.html)

## Using this template

To run: 

`$ cookiecutter git@github.com:um-xr2learn-enablers/XR2Learn-components-cookiecutter-template.git`

Then answer the questions related to the new component that is being created.

This project will create a directory with the new component name in the current directory.

### Questions to answer:
  - "project_name": Name of the Component, following the format: "SSL Features Extraction BM Modality",
  - "description": Description of the component,
  - "project_slug": e.g., "ssl_features_extraction_bm_modality",
  - "component_folder": e.g., "SSL_Features_Extraction_BM_Modality",
  - "parent_component": Parent Component Name e.g., "Pre_precessing",
  - "main_python_file": Python entry-point script name without .py format, e.g., `generate_features.py`
  - "service_name": e.g., "ssl-features-generation-bm",
  - "current_version": Repository current version in the format: "0.1.0"



## What's inside

* Fully running component skeleton
* Component ENVVARS read from .env file
* Unit tests setup
* Documentation

