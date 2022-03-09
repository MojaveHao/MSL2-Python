def read_config():
    with open("msl_config.txt") as f:
        temp = f.read()
    return (temp["ujv"],temp[0]["jp"],temp[0]["sp"],temp[0]["dp"])
def write_config(ujv,jp,sp,dp):
    with open("msl_config.txt","w") as f:
        f.write(f"['ujv':{ujv},'jp':{jp},'sp':{sp},'dp':{dp}]")