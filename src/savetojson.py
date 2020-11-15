# Script that takes a string as input
# converts each character to binary
# and writes an array of binary to a json file

import os
import json
from json import JSONEncoder
import numpy


def main():
    strToJson()


def strToJson():
    string = "An example"

    binary_arr = bytearray(string, "utf8")

    binary = []

    for byte in binary_arr:
        binary_representation = bin(byte)
        binary.append(binary_representation)

    saveJson(binary)


def saveJson(binary):
    # class NumpyArrayEncoder(JSONEncoder):
    #     def default(self, obj):
    #         if isinstance(obj, numpy.ndarray):
    #             return obj.tolist()
    #         return JSONEncoder.default(self, obj)

    data = {"binary": binary}

    # Write data into file
    with open("binary.json", "w") as write_file:
        json.dump(data, write_file)


if __name__ == "__main__":
    main()
