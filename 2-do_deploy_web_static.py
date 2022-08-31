#!/usr/bin/python3
"""
With Fabric , create a tgz archive
from web_static content folder
"""

from fabric.api import env, local, put, run
from datetime import datetime
from os.path import exists, isdir
env.hosts = ['3.80.49.230', '204.236.197.173']
env.user = 'ubuntu'

def do_pack():
        """ The function do_pack """
        local("mkdir -p versions")
        time = datetime.strftime(datetime.now(), "%Y%m%d%H%M%S")
        filename = "versions/web_static_{}.tgz".format(time)
        try:
                local("tar -czvf {} web_static".format(filename))
                return filename
        except Exception:
                return None


def do_deploy(archive_path):
        """ The function do_deploy """
        if not exists(archive_path):
                return False
        try:
                """archive_path = versions/web_static_20170315003959.tgz """
                file_name = archive_path.split("/")[-1]
                "file_name = web_static_20170315003959.tgz"""
                no_ext = file_name.split(".")[0]
                """no_ext = web_static_20170315003959"""
                path = "/data/web_static/releases/"
                """Upload the archive to the /tmp/ directory of the web server"""
                put(archive_path, '/tmp/')
                run('mkdir -p {}{}/'.format(path, no_ext))
                """Uncompress the archive"""
                run('tar -xzf /tmp/{} -C {}{}/'.format(file_name, path, no_ext))
                run('rm /tmp/{}'.format(file_name))
                run('mv {0}{1}/web_static/* {0}{1}/'.format(path, no_ext))
                run('rm -rf {}{}/web_static'.format(path, no_ext))
                run('rm -rf /data/web_static/current')
                run('ln -s {}{}/ /data/web_static/current'.format(path, no_ext))
                print("New version deployed!")
                return True
        except Exception:
                return False
