# github-repo-backup

#### Features
- Auto backup your repos easily
- A fork of [this](https://gist.github.com/Vulcalien/b631e1fe471a6baf07f1943f70434657)

## Running with Docker
#### Using Docker Compose

```yaml
version: '2'
services:
  github-repo-backup:
    image: ghcr.io/infra-blue/github-repo-backup:main
    container_name: github-repo-backup
    volumes:
      - "path-to-your-settings.yaml" : /github-repo-backup/config/settings.yaml
      - "path-to-your-backup-folder" : /github-repo-backup/backup
    restart: unless-stopped

```
#### Building and running locally

1. Clone the repository:
```bash
$ git clone git@github.com:infra-blue/github-repo-backup.git
```
2. Make a copy of `config/settings.yaml.dist` and rename it to `config/settings.yaml`.
3. Change `user` field with your github username
4. You can even change `skip_forks` field and `auto-update-time` field (in minutes)
5. Build the image:
```bash
    $ cd github-repo-backup
    $ docker build -t github-repo-backup .
```
6. Run:

   - On Windows:
     ```bash
     $ docker run -v "C:\path\to\your\settings.yaml":"/github-repo-backup/config/settings.yaml" -v "C:\path-to-your-backup-folder":"/github-repo-backup/backup" github-repo-backup
     ```
     
   - On Linux:
     ```bash
     $ docker run -v "/path/to/your/settings.yaml":"/github-repo-backup/config/settings.yaml" -v "path-to-your-backup-folder":"/github-repo-backup/backup" github-repo-backup
     ```

### Pull image from remote repository and run

```bash
$ docker run --name github-repo-backup -v "/local/path/to/settings.yaml":"/github-repo-backup/config/settings.yaml" -v "path-to-your-backup-folder":"/github-repo-backup/backup" -t ghcr.io/infra-blue/github-repo-backup:main
```

### Running Natively

1. Clone this repository.
2. Copy `config/settings.yaml.dist` to `config/settings.yaml`.
3. Change `user` field with your github username
4. You can even change `skip_forks` field and `auto-update-time` field (in minutes)
5. Execute: 
```bash
$ python main.py
```

### Credits
- [Leonardo Mirabella](https://github.com/infra-blue)
- [Vulcalien](https://github.com/Vulcalien)