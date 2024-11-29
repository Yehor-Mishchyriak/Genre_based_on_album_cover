from json import load

def load_json_config(config_location: str) -> dict:
    with open(config_location, "r") as config_file:
        config = load(config_file)
    return config
