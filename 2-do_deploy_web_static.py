#!/usr/bin/python3
"""
a Fabric script that generates a .tgz archive
from the contents of the web_static folder
"""
import os
from fabric.api import run
from fabric.api import put
from fabric.api import env
from fabric.api import local
from datetime import datetime



env.hosts = ['52.91.152.165', '3.85.33.67']
env.user = 'ubuntu'
env.key_filename = '~/.ssh/id_rsa.pem'

def do_deploy(archive_path):
    """Distribute an archive to the web servers and deploy it"""

    if not os.path.exists(archive_path):
        return False

    try:
        archive_name = os.path.basename(archive_path)
        release_dir = "/data/web_static/releases/"
        release_folder = "{}{}".format(release_dir, archive_name[:-4])
        current_dir = "/data/web_static/current"

        put(archive_path, "/tmp/")

        run("sudo mkdir -p {}".format(release_folder))

        run("sudo tar -xzf /tmp/{} -C {}".format(archive_name, release_folder))

        run("sudo rm /tmp/{}".format(archive_name))

        run("sudo mv {}/web_static/* {}".format(release_folder, release_folder))

        run("sudo rm -rf {}/web_static".format(release_folder))

        run("sudo rm -rf {}".format(current_dir))

        run("sudo ln -s {} {}".format(release_folder, current_dir))
        
        print("New version deployed!")
        return True

    except Exception as e:
        print(e)
        return False
