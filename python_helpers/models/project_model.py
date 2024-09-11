# ############################
#  File Name: $file.name     #
#  Author: Kasper de Bruin   #
#  Date:  2024 - 9 - 10      #
#  Description:              #
#  Copyright (c) 2024.       #
# ############################
from typing import List

from rich.table import Table

from ..models.module_model import ModuleModel
from ..console import console

from rich.panel import Panel
from rich.console import Text
from rich.console import Group

class UProjectModel:
    """"
    Wrapper around unreal project data.
    """

    def __init__(self, name: str, author: str, path: str, modules: List[ModuleModel]):
        """
        Constructs the project model.

        :param name: The name of the project.
        :type name: str
        :param author: The author of the project.
        :type author: str
        :param path: The path to the project.
        :type path: str
        :param modules: The modules of the project.
        :type modules: List[ModuleModel]
        """
        self.name = name
        self.author = author
        self.path = path
        self.modules = modules


    def print(self):
        """
        Print the project data in a cool format
        """
        # Create a rich Text for the header
        header_text = Text(f"Project: {self.name}", style="bold yellow")
        author_text = Text(f"Author: {self.author}", style="bold green")
        path_text = Text(f"Path: {self.path}", style="italic blue")

        # Create the table for modules
        table = Table(title="Modules", expand=True)
        table.add_column("Name", style="cyan", no_wrap=True)
        table.add_column("Type", style="magenta", no_wrap=True)
        table.add_column("Created By", style="green", no_wrap=True)
        table.add_column("Path", style="blue", overflow="fold")

        for module in self.modules:
            table.add_row(module.name, module.module_type, module.created_by, module.path)

        # Group the header and table
        group = Group(header_text, author_text, path_text, table)

        # Wrap everything in a Panel
        panel = Panel(group, title="Project Overview", border_style="bold yellow")

        # Print the panel using console
        console.print(panel)