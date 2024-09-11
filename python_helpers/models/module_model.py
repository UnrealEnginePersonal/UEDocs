# ############################
#  File Name: $file.name     #
#  Author: Kasper de Bruin   #
#  Date:  2024 - 9 - 11      #
#  Description:              #
#  Copyright (c) 2024.       #
# ############################


class ModuleModel:
    """
    Wrapper around unreal model data.
    """

    def __init__(self, name: str, module_type: str, created_by: str, path: str):
        """
        Constructs the module model.

        :param name: The name of the module.
        :type name: str
        :param module_type: The type of the module.
        :type module_type: str
        :param created_by: The author of the module.
        :type created_by: str
        :param path: The path to the module.
        :type path: str
        """
        self.name = name
        self.module_type = module_type
        self.created_by = created_by
        self.path = path
