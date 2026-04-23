import re
import sys

MODULE_REGEX = r'^[_a-zA-Z][_a-zA-Z0-9]*$'

module_name = '{{ cookiecutter.module_name }}'
project_slug = '{{ cookiecutter.project_slug }}'

if not re.match(MODULE_REGEX, module_name):
    print(f'ERROR: "{module_name}" is not a valid Python module name!')
    print('Module names must start with a letter or underscore and contain only letters, numbers, and underscores.')
    sys.exit(1)

if not re.match(r'^[a-zA-Z][a-zA-Z0-9-]*$', project_slug):
    print(f'ERROR: "{project_slug}" is not a valid project slug!')
    print('Project slugs must start with a letter and contain only letters, numbers, and hyphens.')
    sys.exit(1)