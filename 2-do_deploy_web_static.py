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


def do_pack():
	"""generates a .tgz archive from the contents of the web_static folder
	"""
	time = datetime.now().strftime("%Y%m%d%H%M%S")
	os.makedirs("versions") if not os.path.exists("versions") else None

	archive_name = "web_static_" + time + ".tgz"
	archive_path = local("tar -czvf versions/{} web_static".format(archive_name))

	return "versions/" + archive_name if archive.succeeded else None

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
        
        # Create the release directory
        run("mkdir -p {}".format(release_folder))
        
        # Uncompress the archive into the release folder
        run("tar -xzf /tmp/{} -C {}".format(archive_name, release_folder))
        
        # Delete the uploaded archive
        run("rm /tmp/{}".format(archive_name))
        
        # Move the contents from the release folder to current folder
        run("mv {}/web_static/* {}".format(release_folder, release_folder))
        
        # Remove the empty web_static folder
        run("rm -rf {}/web_static".format(release_folder))
        
        # Delete the symbolic link 'current'
        run("rm -rf {}".format(current_dir))
        
        # Create a new symbolic link
        run("ln -s {} {}".format(release_folder, current_dir))
        
        print("New version deployed!")
        return True

    except Exception as e:
        print(e)
        return False
