"""
File name: SETUP.py
Author: Kasper de Bruin
Created: 2024-10-09
Version: 0.1
"""

import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), "python_helpers"))

from typing import List
import rich
from rich.table import Table

import rich_click as click

from python_helpers.console import console

from python_helpers.models.project_model import UProjectModel

from python_helpers.project_generator import ProjectGenerator
from python_helpers.UEProjectUtil import UEProjectUtil

# Use Rich markup
click.rich_click.USE_RICH_MARKUP = True

script_root_dir: str = os.path.dirname(os.path.realpath(__file__))
game_project_root: str = os.path.abspath(os.path.dirname(script_root_dir))

def cli():
    """
    Set up the Docs for Unreal Engine project.
    """
    # get the project data
    project_data: UProjectModel = UEProjectUtil.get_project_data(game_project_root)

    # print the project data
    project_data.print()

    # generate the docs
    generator = ProjectGenerator(project=project_data)
    generator.generate_project(game_project_root)

if __name__ == "__main__":
    cli()
