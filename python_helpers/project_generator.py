"""
File name: project_generator.py
Author: Kasper de Bruin
Created: 2024-10-09
Version: 0.1
"""
import os
from console import console
import shutil

class ProjectGenerator:
    def __init__(self, project_name: str, author: str, copy_right: str, setup_cmake: bool, is_project: bool, is_plugin: bool):
        self.project_name = project_name
        self.author = author
        self.copy_right = copy_right
        self.setup_cmake = setup_cmake
        self.is_project = is_project
        self.is_plugin = is_plugin

    def setup_cmake_file(self, docs_dir: str, root_dir: str):
        console.print(f"Setting up CMakeLists.txt in: {docs_dir}")
        #copy the CMakeLists.txt.in file to the root_dir
        shutil.copyfile(os.path.join(docs_dir, "CMakeLists.txt.in"), os.path.join(root_dir, "CMakeLists.txt"))

        with open(os.path.join(docs_dir, "CMakeLists.txt.in"), "r") as file:
            file_data = file.read()
            file_data = file_data.replace("@IN_PROJECT_NAME@", self.project_name)
            file.close()

        with open(os.path.join(root_dir, "CMakeLists.txt"), "w") as file:
            file.write(file_data)

    def setup_index_rst(self, docs_dir: str):
        console.print(f"Setting up index.rst in: {docs_dir}")
        #copy the index.rst.in file to the root_dir
        shutil.copyfile(os.path.join(docs_dir, "index.rst.in"), os.path.join(docs_dir, "index.rst"))

        with open(os.path.join(docs_dir, "index.rst.in"), "r") as file:
            file_data = file.read()
            file_data = file_data.replace("@IN_PROJECT_NAME@", self.project_name)
            file.close()

        with open(os.path.join(docs_dir, "index.rst"), "w") as file:
            file.write(file_data)
            file.close()

    def setup_conf_file(self, docs_dir: str):
        console.print(f"Setting up conf file in: {docs_dir}")
        #copy the conf.py.in file to the root_dir

        conf_file = os.path.join(docs_dir, "conf.py.in")
        shutil.copyfile(conf_file, os.path.join(docs_dir, "conf.py"))

        #open the conf.py file and replace the values
        with open(os.path.join(docs_dir, "conf.py"), "r") as file:
            filedata = file.read()
            filedata = filedata.replace("@IN_PROJECT_FINAL_NAME@", self.project_name)
            filedata = filedata.replace("@IN_PROJECT_AUTHOR@", self.author)
            filedata = filedata.replace("@IN_PROJECT_COPYRIGHT@", self.copy_right)
            file.close()

        with open(os.path.join(docs_dir, "conf.py"), "w") as file:
            file.write(filedata)
            file.close()


    def generate_project(self, root_dir: str):
        console.print(f"Generating project: {self.project_name}")
        console.print(f"Author: {self.author}")
        console.print(f"Copy right: {self.copy_right}")
        console.print(f"Setup CMake: {self.setup_cmake}")
        console.print(f"Is project: {self.is_project}")
        console.print(f"Is plugin: {self.is_plugin}")
        console.print(f"Root dir: {root_dir}")
        docs_dir = os.path.join(root_dir, "Docs")
        console.print(f"Docs dir: {docs_dir}")

        #setup the conf file
        self.setup_conf_file(docs_dir)

        #setup the index.rst file
        self.setup_index_rst(docs_dir)

        if self.setup_cmake:
            self.setup_cmake_file(docs_dir, root_dir)

        console.print("Project generated.")

