from subprocess import call

from pip._internal.utils.misc import get_installed_distributions

if __name__ == '__main__':
    for dist in get_installed_distributions():
        package_name = dist.project_name
        print('{}updating package {}'.format('--------------------\n', package_name))
        call("pip install --upgrade " + package_name, shell=True)
        print('√')
