#!/usr/bin/python3
"""
a Fabric script that generates a .tgz archive
from the contents of the web_static folder
"""
import os
from fabric.api import local
from datetime import datetime


def do_pack():
	"""
	generates a .tgz archive from the contents of the web_static folder
	"""
	time = datetime.now().strftime("%Y%m%d%H%M%S")
	os.makedirs("versions") if not os.path.exists("versions") else None

	archive_name = "web_static_" + time + ".tgz"
	archive = local("tar -czvf versions/{} web_static".format(archive_name))

	return "versions/" + archive_name if archive.succeeded else None

if __name__ == "__main__":
	do_pack()
