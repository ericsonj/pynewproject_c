import datetime
from pathlib import Path
import os
from pymakelib.new_project import Generator

temp_name = 'c_project'

temp_files = [
    'app/inc/main.h',
    'app/src/main.c',
    'app/app_mk.py',
    'makefile.mk',
    'Makefile',
    'Makefile.py',
    ".project",
    ".pymakeproj/.cproject_template",
    ".pymakeproj/.language.settings_template",
    ".settings",
]

temp_tokens = {
    'author':       'Ericson Joseph',
    'date':         datetime.datetime.now().strftime('%b-%d-%I%M%p-%G'),
    'project_name': 'c_temp'
}

def get_generator() -> Generator:

    author = input("Your name: ")
    project_name = input("Your project name: ")

    temp_tokens['author'] = author
    temp_tokens['project_name'] = project_name

    output_dir = Path( Path(os.getcwd()) / Path(project_name))
    print(temp_tokens)
    print(str(output_dir))

    return Generator("c_project", "/tmp/c_project.tar.gz", temp_files, temp_tokens, output_dir) 