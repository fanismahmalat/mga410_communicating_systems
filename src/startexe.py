import os
import pathlib
import subprocess


# os.startfile("convowithpython.exe")


def executeProcessingSystem():
    os.chdir(os.path.abspath("./processing-system/executable"))
    os.system("convowithpython.exe")
