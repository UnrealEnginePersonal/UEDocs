"""
File name: project_generator.py
Author: Kasper de Bruin
Created: 2024-10-09
Version: 0.1
"""

import os
import shutil
from typing import Dict

from .models.project_model import UProjectModel


def setup_file(src_filename: str, dest_filename: str, replacements: Dict[str, str]):
    """
    General method to copy and replace placeholders in a file.
    """
    shutil.copyfile(src_filename, dest_filename)

    if replacements:
        with open(dest_filename, "r") as file:
            content = file.read()
        for placeholder, value in replacements.items():
            content = content.replace(placeholder, value)

        with open(dest_filename, "w") as file:
            file.write(content)


class ProjectGenerator:
    """
    Generator for the Docs project.
    """
    doc_template_dir = "DocFiles"

    def __init__(self, project: UProjectModel):
        """
        Initialize the project generator.
        """
        self.project = project

    @staticmethod
    def get_template_dir(docs_dir: str) -> str:
        """
        Get the template directory.
        """
        return os.path.join(docs_dir, ProjectGenerator.doc_template_dir)

    def setup_cmake_file(self, docs_dir: str, root_dir: str):
        """
        Set up the CMakeLists.txt file.
        """
        cmake_file = os.path.join(self.get_template_dir(docs_dir), "CMakeLists.txt.root.in")
        dest_file = os.path.join(root_dir, "CMakeLists.txt")
        setup_file(cmake_file, dest_file, {"@IN_PROJECT_NAME@": self.project.name})

    def setup_index_rst(self, docs_dir: str):
        """
        Set up the index.rst file.
        """
        index_file = os.path.join(self.get_template_dir(docs_dir), "index.rst.in")
        dest_file = os.path.join(docs_dir, "index.rst")
        setup_file(index_file, dest_file, {"@IN_PROJECT_NAME@": self.project.name})

    def setup_conf_file(self, docs_dir: str):
        """
        Set up the conf.py file.
        """
        conf_file = os.path.join(self.get_template_dir(docs_dir), "conf.py.in")
        dest_file = os.path.join(docs_dir, "conf.py")
        setup_file(conf_file, dest_file, {
            "@IN_PROJECT_FINAL_NAME@": self.project.name,
            "@IN_PROJECT_AUTHOR@": self.project.author,
            "@IN_PROJECT_COPYRIGHT@": self.project.author
        })

    def generate_project(self, root_dir: str):
        """
        Generate the project in the root dir.
        """
        docs_dir = os.path.join(root_dir, "Docs")
        self.setup_conf_file(docs_dir)
        self.setup_index_rst(docs_dir)
        self.setup_introduction_rst(docs_dir)
        self.setup_cmake_file(docs_dir, root_dir)

    def setup_introduction_rst(self, docs_dir: str):
        """
        Sets up the introduction.rst file.
        """
        pass
