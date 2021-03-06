# coding=utf-8
from datetime import datetime
from os.path import isfile

from fabric.api import sudo, run, env, cd, local, settings, prefix, task


env.directory = '~/webapps/corpecumig/corporacion'
env.activate = 'source ~/.virtualenvs/corpecumig/bin/activate'
env.hosts = ['corpecumig.com', ]
env.project = 'corpecumig'
env.user = 'pro'


@task
def upgrade():
    """
        Update server content
    """

    with settings(warn_only=True):
        local("git push")

    with cd(env.directory):
        run('git pull')
        run('git lfs pull')
        with prefix(env.activate):
            run('pip install -r ../requirement/production.txt')
            run('python manage.py migrate --settings=corporacion.settings.production')
            run('python manage.py collectstatic -l --noinput --settings=corporacion.settings.production')
        sudo("supervisorctl restart %s" % env.project)


@task
def backup():
    now = datetime.now()
    file_name = 'mundosportec_%s.out' % now.strftime("%Y-%m-%d_%Hh")  # :%M:%S

    if not isfile('/home/pro/backups/%s' % file_name):
        # Genera el respaldo
        with cd('~/backups'):
            sudo('sudo -u postgres pg_dump mundosportec > %s' % file_name)
        # Descarga el archivo
        # local('scp pytel@server.cacperu.com:%s /home/pro/' % file_name)
    # Ejecuta el respaldo
    # local('sudo -u postgres psql -f /home/pro/%s' % file_name)


# @task
# def call_command(command):
#     """
#         Ejecuta un comando de manage.py:
#         $ fab call_command:"migrate"
#     """

#     with settings(warn_only=True):
#         local("hg push")

#     with cd(env.directory):
#         run('hg pull -u')
#         with prefix(env.activate):
#             run('python manage.py %s' % command)


# @task
# def call(command):
#     """
#         Ejecuta un comando de manage.py ejm:
#         $ fab call:"migrate"
#     """

#     with cd(env.directory):
#         with prefix(env.activate):
#             run('python manage.py %s' % command)
