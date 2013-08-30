from distutils.core import setup

from objfetch import __version__

setup(
    name = 'objfetch',
    description = 'A tool to translate objects to dict&list style.',
    version = __version__,
    author = 'cfrco',
    author_email = 'z82206.cat@gmail.com',
    packages = ['objfetch']
)
