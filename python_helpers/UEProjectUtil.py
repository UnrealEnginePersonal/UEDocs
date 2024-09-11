# ############################
#  File Name: $file.name     #
#  Author: Kasper de Bruin   #
#  Date:  2024 - 9 - 10      #
#  Description:              #
#  Copyright (c) 2024.       #
# ############################

import os

from .models.module_model import ModuleModel
from .models.project_model import UProjectModel

from console import console
from typing import List


class UEProjectUtil:
    @staticmethod
    def get_project_data(game_root_dir: str) -> UProjectModel:
        """
        Get the project data from the project file.
        """
        import json
        # check if root dir contains .uproject
        project_file = None

        for file in os.listdir(game_root_dir):
            if file.endswith(".uproject"):
                project_file = file
                break

        # try to get uplugin file
        if project_file is None:
            for file in os.listdir(game_root_dir):
                if file.endswith(".uplugin"):
                    project_file = file
                    break

        if project_file is None:
            raise Exception(f"No UPLUGIN or UPROJECT file found in the root directory {game_root_dir}")

        path = os.path.join(game_root_dir, project_file)
        with open(path, "r", encoding='utf-8-sig') as file:
            project_json = json.load(file)
            file.close()

            author = project_json["CreatedBy"]
            project_name = project_json["FriendlyName"]

            modules: List[ModuleModel] = []
            if "Modules" in project_json:
                for module in project_json["Modules"]:
                    module_name: str = module["Name"]
                    module_type: str = module["Type"]
                    modules.append(ModuleModel(
                        module_name,
                        module_type,
                        author,
                        os.path.join(game_root_dir, module_name)
                    ))



        return UProjectModel(
            project_name,
            author,
            game_root_dir,
            modules
        )