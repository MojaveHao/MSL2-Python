import json

def read_config():
    with open("config.json","r") as f:
        conf = json.load(f)
        return conf
    
def write_config(config):
    with open("msl_config.json", "w+") as f:
        print(config)
        json.dump(config, f, ensure_ascii=False, sort_keys=True, indent=4, separators=(',', ': '))