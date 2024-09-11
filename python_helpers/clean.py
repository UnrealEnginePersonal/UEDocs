# ############################
#  File Name: $file.name     #
#  Author: Kasper de Bruin   #
#  Date:  2024 - 9 - 10      #
#  Description:              #
#  Copyright (c) 2024.       #
# ############################

def clean_up_docs():
    """
    Clean up the doc's folder.

    This will remove generated_files conf.py, index.rst, cmakelist.txt, doxyfile and _build
    """
    import os
    import shutil
    docs_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
    print(f"Cleaning up docs folder: {docs_dir}")

    # remove the generated files
    files = ["conf.py", "index.rst", "CMakeLists.txt", "Doxyfile"]
    for file in files:
        path = os.path.join(docs_dir, file)
        if os.path.exists(path):
            os.remove(path)

    # remove the _build folder
    build_dir = os.path.join(docs_dir, "_build")
    if os.path.exists(build_dir):
        shutil.rmtree(build_dir)

    # remove the generated_files folder
    generated_files_dir = os.path.join(docs_dir, "generated_api")
    if os.path.exists(generated_files_dir):
        shutil.rmtree(generated_files_dir)

    print("Cleaned up docs folder")

if __name__ == "__main__":
    clean_up_docs()