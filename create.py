from os import write
import yaml
import ruamel.yaml

manufacturer = "TestManufacturer"
model = "test"
slug = "test"

device = {
    "manufacturer": manufacturer,
    "model": model,
    "slug": slug,
    "u_height": 1,
    "is_full_depth": False,
    "interfaces": [],
    "console-ports": [],
    "power-ports":[]
}

device['interfaces'].append({"name": "eth0","type": "1000base-t", "mgmt_only": False})
device['interfaces'].append({"name": "eth1","type": "1000base-t", "mgmt_only": False})
device['interfaces'].append({"name": "eth2","type": "1000base-t", "mgmt_only": False})
device['interfaces'].append({"name": "eth3","type": "1000base-t", "mgmt_only": False})

yaml_file = open("device-types/"+manufacturer+"/"+model+".yml", "w")
device_yaml = yaml.safe_dump(device, sort_keys=False, explicit_start=True)
data = ruamel.yaml.round_trip_load(device_yaml)
yaml_file.write( '---\n')
for line in ruamel.yaml.round_trip_dump(data, indent=4, block_seq_indent=2).splitlines(True):
    yaml_file.write(line)
yaml_file.close()
