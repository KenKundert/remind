from setuptools import setup
from codecs import open

with open('README.rst', encoding='utf-8') as f:
    readme = f.read()

setup(
    name = 'schedule-reminder',
    version = '0.3.0',
    description = 'reminder program',
    long_description = readme,
    long_description_content_type='text/x-rst',
    author = "Ken Kundert",
    author_email = 'remind@nurdletech.com',
    url = 'https://github.com/kenkundert/remind',
    download_url = 'https://github.com/kenkundert/remind/tarball/master',
    license = 'GPLv3+',
    scripts = 'remind'.split(),
    py_modules = 'quantiphy'.split(),
    install_requires = 'docopt inform quantiphy arrow'.split(),
    python_requires = '>=3.6',
)
