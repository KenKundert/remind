from setuptools import setup
from codecs import open

with open('README.rst', encoding='utf-8') as f:
    readme = f.read()

setup(
    name = 'alarm',
    version = '0.0.3',
    description = 'reminder program',
    long_description = readme,
    author = "Ken Kundert",
    author_email = 'alarm@nurdletech.com',
    url = 'https://github.com/kenkundert/alarm',
    download_url = 'https://github.com/kenkundert/alarm/tarball/master',
    license = 'GPLv3+',
    scripts = 'alarm'.split(),
    py_modules = 'quantiphy'.split(),
    install_requires = 'docopt inform quantiphy arrow'.split(),
    python_requires = '>=3.6',
)
