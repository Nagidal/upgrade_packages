# How to upgrade all Python packages with pip?
# Solution from Stack Overflos
# URL: https://stackoverflow.com/questions/2720014/how-to-upgrade-all-python-packages-with-pip
# Answer https://stackoverflow.com/a/5839291/9235421
# by Ramana (https://stackoverflow.com/users/515656/ramana)

import pkg_resources
from subprocess import call

packages = [dist.project_name for dist in pkg_resources.working_set]
call("pip install --upgrade " + ' '.join(packages), shell=True)
