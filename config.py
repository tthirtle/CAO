import configparser
import sys
import os
if sys.platform.startswith("win"):
    config_file = "config.ini"
else:
    config_file = f"{os.environ.get('HOME')}/.tp/config.ini"
    if os.listdir(os.environ.get('HOME')).count('.tp') == 0:
        os.mkdir(f"{os.environ.get('HOME')}/.tp")

def save_config():
    import _global
    config = configparser.ConfigParser()
    config['CAO'] = _global.config
    with open(config_file,'w') as configfile:
        config.write(configfile)

def config_exist():
    try:
        with open(config_file):
            pass
        return True
    except:
        return False

def load_config():
    if config_exist() == False:
        return
    import _global
    config = configparser.ConfigParser()
    config.read(config_file)
    _global.config.update({"Company":config.get('CAO',"Company")})
    _global.config.update({"Database":config.get('CAO',"Database")})
    _global.config.update({"Reports":config.get('CAO',"Reports")})