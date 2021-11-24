
import sys
# https://yaml.readthedocs.io/en/latest/install.html
from ruamel.yaml import YAML
# import yaml
from pprint import pprint

with open('d:\\netbox_device_types_.yaml', encoding='utf-8') as f, open('d:\\netbox_device_types.csv', 'w', encoding='utf-8') as dest:
    # content = yaml.load(f, Loader=yaml.FullLoader)

    yaml = YAML(typ='safe')
    for data in yaml.load_all(f):
        line = f"{data['manufacturer']};{data['model']}; {data['slug']};{data['part_number']};{data['u_height']}\n"
        dest.write(line)


# pprint(content)
