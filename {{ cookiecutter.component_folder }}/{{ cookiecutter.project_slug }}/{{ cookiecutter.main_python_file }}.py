# Your Python code here

from conf import MAIN_FOLDER


def call_component():
    print(MAIN_FOLDER)
    print('Call component {{ cookiecutter.project_name }}')


if __name__ == '__main__':
    call_component()
