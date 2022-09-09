file_path = ''
log_name = 'server.log'
def incoming_filepath(filepath:str,logname='server.log'):
    global file_path
    global log_name
    file_path = filepath
    log_name = logname
with open(f'{filepath}{log_name}','r') as f:
    logs = f.readlines()
    