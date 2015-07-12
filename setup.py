try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
    'description': 'pyService Skeleton',
    'author': 'Matthew Lauber',
    'url': 'https://github.com/mklauber/pyService',
    'download_url': 'git@github.com:mklauber/pyService.git',
    'author_email': 'github.com@mklauber.com',
    'version': '1.0',
    'install_requires': ['nose'],
    'packages': ['pyService'],
    'scripts': [],
    'name': 'pyService'
}

setup(**config)
