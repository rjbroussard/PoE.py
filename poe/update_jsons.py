import json as js
import os

from poe import Client

_dir = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'data')


def update_keystones():
    cl = Client()
    ks = cl.find_passives({'is_keystone': "1"})
    ks_json = {node.int_id: node.name for node in ks}

    with open(f"{_dir}/keystones.json", 'w+') as file:
        js.dump(ks_json, file)


def update_ascendancy():
    cl = Client()
    asc = cl.find_passives({'_pageName': "Passive Skill:Ascendancy%"}, limit=500)
    asc_json = {node.int_id: node.name for node in asc}

    with open(f"{_dir}/ascendancy.json", 'w+') as file:
        js.dump(asc_json, file)


if __name__ == "__main__":
    update_keystones()
    update_ascendancy()
    print("Done!")
