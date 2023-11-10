"""Config module"""
import yaml
from typing import TypedDict

class Config(TypedDict):
    user: str
    skip_forks: bool
    auto_update_time: int

with open('config/settings.yaml', 'r', encoding='utf-8') as yaml_config:
    config_map: Config = yaml.load(yaml_config, Loader=yaml.SafeLoader)
