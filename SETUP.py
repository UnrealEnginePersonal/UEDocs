"""
File name: SETUP.py
Author: Kasper de Bruin
Created: 2024-10-09
Version: 0.1
"""
import os

#add python_helpers to the path
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), "python_helpers"))

import rich_click as click

from python_helpers.project_generator import ProjectGenerator
from python_helpers.UEProjectUtil import UEProjectUtil

# Use Rich markup
click.rich_click.USE_RICH_MARKUP = True

script_root_dir: str = os.path.dirname(os.path.realpath(__file__))
game_project_root: str = os.path.abspath(os.path.dirname(script_root_dir))

def run_setup(project_name: str, author: str, copyr: str, cmake: bool):
    generator = ProjectGenerator(project_name, author, copyr, cmake, True, False)
    generator.generate_project(game_project_root)

def ask_for_project_name() -> str:
    """
    Ask for the project name.
    :return: The project name.
    """
    return click.prompt("Enter the project name", type=str)


def ask_for_author_name() -> str:
    """
    Ask for the author name.
    :return: The author name.
    """
    return click.prompt("Enter the author name", type=str)


def ask_for_copy_right() -> str:
    """
    Ask for the copy right.
    :return: The copy right.
    """
    return click.prompt("Enter the copyright", type=str)


def ask_for_cmake() -> bool:
    """
    Ask if the user wants to setup the CMakeLists.txt file.
    :return: True if the user wants to setup the CMakeLists.txt file.
    """
    return click.confirm("Do you want to setup the CMakeLists.txt file?")


@click.command()
@click.option(
    "--project",
    type=click.STRING,
    help="The project name",
    required=False
)
@click.option(
    "--author",
    type=click.STRING,
    help="The project author",
    required=False
)
@click.option(
    "--copyr",
    type=click.STRING,
    help="The project copy right",
    required=False
)
@click.option(
    "--cmake",
    type=click.BOOL,
    help="Also setup the CMakeLists.txt file",
    required=False
)
def cli(project, author, copyr, cmake):
    """
    Set up the Docs for Unreal Engine project.
    """
    project_name = project
    author_name = author
    copy_right = copyr
    setup_cmake = cmake

    if project_name is None or author_name is None or copy_right is None or setup_cmake is None:
        project_data: dict = UEProjectUtil.get_project_data(game_project_root)
        project_name = UEProjectUtil.get_project_name(project_data)
        author_name = UEProjectUtil.get_author_name(project_data)
        copy_right = f"2024. All rights reserved. {author_name}"



    if project_name is None:
        project_name = ask_for_project_name()

    if author_name is None:
        author_name = ask_for_author_name()

    if copy_right is None:
        copy_right = ask_for_copy_right()

    if setup_cmake is None:
        setup_cmake = ask_for_cmake()

    run_setup(project_name, author_name, copy_right, setup_cmake)


if __name__ == "__main__":
    cli()
