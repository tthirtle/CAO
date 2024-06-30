def save_config(company:str,dbase:str,report:str):
    import _global
    import config
    _global.config.update({"Company":company})
    _global.config.update({"Database":dbase})
    _global.config.update({"Reports":report})
    config.save_config()

def load_config():
    import config
    config.load_config()

def get_comp():
    import _global
    return _global.config.get("Company")

def get_dbase():
    import _global
    return _global.config.get("Database")

def get_report_dir():
    import _global
    return _global.config.get("Reports")

def get_all_states():
    import address
    return address.get_all_states_name()