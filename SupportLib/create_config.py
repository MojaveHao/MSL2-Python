def read_config():
    with open("msl_config.txt") as f:
        config = eval(f.read())
        return config
'''
{
    'server_name':'',
    'server_path':''
    'java_path':'',
}
'''
def write_config(config):
    with open("msl_config.txt", "w") as f:
        old_config = read_config()
        for con in old_config:
            if config == con:
                print("Config Already Saved.")
                exit()
        new_config = old_config.append(config)
        f.write(new_config)