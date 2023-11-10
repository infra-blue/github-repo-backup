"""Backup module"""
import os
import json

from urllib.request import urlopen
from modules.config import config_map

def backup_task() -> None:
    with urlopen('https://api.github.com/users/' + config_map['user'] + '/repos') as repo:
        repos_list = json.loads(repo.read())

    for repo in repos_list:
        print('\033[31m' + repo['name'] + '\033[m')
        if repo['fork'] and config_map['skip_forks']:
            print('Fork: skipping')
            continue

        if not os.path.exists(repo['name'] + '.git'):
            print('Repo: create')
            os.system('git clone --mirror -- "' + repo['clone_url'] + '"')
        else:
            print('Repo: update')
            os.chdir(repo['name'] + '.git')
            os.system('git remote update')
            os.chdir('..')
