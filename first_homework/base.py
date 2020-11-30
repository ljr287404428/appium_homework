import yaml


class Base:
    def open_yaml(self):
        with open("./add_contact.yaml",encoding="utf-8") as f:
            return yaml.load(f)