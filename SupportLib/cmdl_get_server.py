import requests
def get_file_url(type="PaperSpigot",ver="1.12.2"):
    can_be_use_type = [
	"PaperSpigot",
	"SpongeForge",
	"CubeRite",
	"GlowStone",
	"Minecraft_Server",
	"Nukkit",
	"Akarin",
	"BungeeCord",
	"CraftBukkit",
	"BukkitPlugins",
	"TacoSpigot",
	"TorchSpigot",
	"Cauldron",
	"Spigot",
	"Thermos",
	"WaterFall",
	"SpongeVanilla"
]
    other_name = ["Paper","Forge","Mojang","Bukkit","Vanilla"]
    if type in can_be_use_type:
        url = f'https://mirror.zerodream.net/?action=getlist&version={type}'
        response = requests.get(url)
        response.encoding = 'utf-8'
        temp = response.text
        tmp = eval(temp)
        for i in tmp:
            if ver in i["name"]:
                return (i["file"],i["name"])
    
    else:
        if type in other_name:
            if type == "Paper":
                url = f'https://mirror.zerodream.net/?action=getlist&version=PaperSpigot'
                response = requests.get(url)
                response.encoding = 'utf-8'
                temp = response.text
                tmp = eval(temp)
                for i in tmp:
                    if ver in i["name"]:
                        return (i["file"],i["name"])
            if type == "Forge":
                url = f'https://mirror.zerodream.net/?action=getlist&version=SpongeFroge'
                response = requests.get(url)
                response.encoding = 'utf-8'
                temp = response.text
                tmp = eval(temp)
                for i in tmp:
                    if ver in i["name"]:
                        return (i["file"],i["name"])
            if type == "Mojang":
                url = f'https://mirror.zerodream.net/?action=getlist&version=Minecraft_Server'
                response = requests.get(url)
                response.encoding = 'utf-8'
                temp = response.text
                tmp = eval(temp)
                for i in tmp:
                    if ver in i["name"]:
                        return (i["file"],i["name"])
            if type == "Bukkit":
                url = f'https://mirror.zerodream.net/?action=getlist&version=CraftBukkit'
                response = requests.get(url)
                response.encoding = 'utf-8'
                temp = response.text
                tmp = eval(temp)
                for i in tmp:
                    if ver in i["name"]:
                        return (i["file"],i["name"])
            if type == "Vanilla":
                url = f'https://mirror.zerodream.net/?action=getlist&version=SpongeVanilla'
                response = requests.get(url)
                response.encoding = 'utf-8'
                temp = response.text
                tmp = eval(temp)
                for i in tmp:
                    if ver in i["name"]:
                        return (i["file"],i["name"])
        else:
            print(f"Can't find this type of server.\nThere is a list of names:{can_be_use_type}\nOr use this names:{other_name}")
            return None,None