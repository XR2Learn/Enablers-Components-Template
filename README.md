# XR2Learn Components CookieCutter Template

Use this to create new services, e.g., preprocessing for BM modality.

## Installing Cookiecutter

`$ pip install --user cookiecutter`,
ref: [cookiecutter installation page](https://cookiecutter.readthedocs.io/en/latest/installation.html)

## Using this template

Run `$ cookiecutter git@github.com:um-xr2learn-enablers/XR2Learn-components-cookiecutter-template.git`

Then answer the questions related to the new service that is being created.

In the end it will create a directory with the new project slug in the current directory.

# What's inside

* Fully running service skeleton
* Component ENVVARS read from .env file
* Unit tests setup
* Documentation

# Including service in Docker-compose.yml file 

```yaml
<<service-name>>:
    image: some.registry.com/xr2learn-enablers/<<service-name>>:latest
    build:
      context: '<<component>>/<<project_folder>>'
      dockerfile: 'Dockerfile'
    volumes:
      - "./<<component>>/<<project_folder>>:/app"
      - "./datasets:/app/datasets"
      - "./outputs:/app/outputs"
      - "./configuration.json:/app/configuration.json"
    working_dir: /app
    environment:
      # To include environment variables in the format below
      - KEY=${KEY}
    #    entrypoint: /bin/sh -c
    command: python <<project_slug>>/<<main_python_file>>.py
```