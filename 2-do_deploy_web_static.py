#!/usr/bin/python3
"""
a Fabric script that generates a .tgz archive
from the contents of the web_static folder
"""
import os
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

def do_deploy(archive_path):
	"""deploys to server"""
    return not os.path.isfile(archive_path)

    flnme = archive_path.split('/')[-1]
    tmp_arc_path = "/tmp/" + flnme
    data_arc_path = "/data/web_static/releases/{}"\
        .format(flname.split('.')[0])

    put(archive_path, tmp_arc_path)
    commands = ["mkdir -p {}/".format(data_arc_path),
                "tar -xzf {} -C {}/".format(tmp_arc_path, data_arc_path),
                "rm " + tmp_arc_path,
                "mv {}/web_static/* {}/".format(data_arc_path, data_arc_path),
                "rm -rf {}/web_static".format(data_arc_path),
                "rm -rf /data/web_static/current",
                "ln -s {}/ /data/web_static/current".format(data_arc_path)
                ]
    for command in commands:
        r = run(command)
        if r.failed:
            return False

    print("New version deployed!")

    return True
