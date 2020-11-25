import os
import pathlib
import subprocess


def executeProcessingSystem():
    os.chdir(os.path.abspath("./processing-system/executable"))
    os.system("convowithpython.exe")
    os.chdir(os.path.abspath("../../"))
