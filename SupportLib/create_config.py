import json

def read_config():
    with open("config.json","r") as f:
        conf = json.load(f)
        return conf
    
def write_config(config):
    with open("msl_config.json", "w") as f:
        old_config = json.load(f)
        if config == old_config:
            return("Already Saved")
        json.dump(config)