import yaml

def load_config(config_path="C:\\Users\\aramani\\PycharmProjects\\PyRITxAllurexApplause\\config\\config.yaml"):
    with open(config_path, "r") as file:
        return yaml.safe_load(file)