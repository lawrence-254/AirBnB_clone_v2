#!/usr/bin/python3
"""
A Fabric script that generates a .tgz archive from the contents
of the web_static folder.
"""
import os
from fabric.api import local
from datetime import datetime


def do_pack():
    """
    Generates a .tgz archive from the contents of the web_static folder.    
    Returns:
        str: Path to the created archive or None if the operation fails.
    """
    try:
        time = datetime.now().strftime("%Y%m%d%H%M%S")
        versions_dir = "versions"
        os.makedirs(versions_dir, exist_ok=True)

        archive_name = "web_static_" + time + ".tgz"
        archive_path = os.path.join(versions_dir, archive_name)

        local("tar -czvf {} web_static".format(archive_path))

        return archive_path
    except Exception as e:
        print("Error: {}".format(e))
        return None

if __name__ == "__main__":
    do_pack()
