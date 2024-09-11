"""
File name: console.py
Author: Kasper de Bruin
Created: 2024-10-09
Version: 0.1
"""

from rich.console import Console

#console = Console()

# Set up the console with soft_wrap enabled and without extra line endings.
console = Console(soft_wrap=True, no_color=False, force_terminal=True,
                  tab_size=4, markup=True, emoji=True, highlight=True)
