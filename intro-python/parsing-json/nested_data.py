#!/usr/bin/env python
"""Working with nested data hands-on exercise / coding challenge."""


import json
import os


# Get the absolute path for the directory where this file is located "here"
here = os.path.abspath(os.path.dirname(__file__))


with open(os.path.join(here, "interfaces.json")) as file:
    # TODO: Parse the contents of the JSON file into a variable
    json_data = json.loads(file.read())

# TODO: Loop through the interfaces in the JSON data and print out each
# interface's name, ip, and netmask.

for interface in json_data["ietf-interfaces:interfaces"]["interface"]:
    print(interface["name"])
    print(interface["address"][0])
    print(interface["address"][1])
