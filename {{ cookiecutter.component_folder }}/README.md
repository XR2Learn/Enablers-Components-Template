# {{ cookiecutter.project_name }}

{{ cookiecutter.description }}

# Including component in Docker-compose.yml file as a service

```yaml
{{ cookiecutter.service_name }}:
image: some.registry.com/xr2learn-enablers/{{ cookiecutter.service_name }}:latest
build:
  context: '{{ cookiecutter.parent_component }}/{{ cookiecutter.component_folder }}'
  dockerfile: 'Dockerfile'
volumes:
  - "./{{ cookiecutter.parent_component }}/{{ cookiecutter.component_folder }}:/app"
  - "./datasets:/app/datasets"
  - "./outputs:/app/outputs"
  - "${CONFIG_FILE_PATH:-./configuration.json}:/app/configuration.json"
working_dir: /app
environment:
  - EXPERIMENT_ID=${EXPERIMENT_ID:-development-model}
command: python {{ cookiecutter.project_slug }}/{{ cookiecutter.main_python_file }}.py

```
