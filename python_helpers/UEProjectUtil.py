# ############################
#  File Name: $file.name     #
#  Author: Kasper de Bruin   #
#  Date:  2024 - 9 - 10      #
#  Description:              #
#  Copyright (c) 2024.       #
# ############################

import os
from console import console

class UEProjectUtil:
    @staticmethod
    def get_project_data(game_root_dir: str) -> dict:
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

        console.print(f"Found project file: {project_file}")
        path = os.path.join(game_root_dir, project_file)
        console.print(f"Path: {path}")

        with open(path, "r", encoding='utf-8-sig') as file:
            project_json = json.load(file)
            friendly_name = project_json["FriendlyName"]
            created_by = project_json["CreatedBy"]
            file.close()

        return {
            "FriendlyName": friendly_name,
            "CreatedBy": created_by
        }

    @staticmethod
    def get_project_name(project_data: dict) -> str:
        return project_data["FriendlyName"]

    @staticmethod
    def get_author_name(project_data: dict) -> str:
        return project_data["CreatedBy"]
