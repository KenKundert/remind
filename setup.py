from setuptools import setup
from codecs import open

with open('README.rst', encoding='utf-8') as f:
    readme = f.read()

setup(
    name = 'schedule-reminder',
    version = '1.1',
    author = "Ken Kundert",
    author_email = 'remind@nurdletech.com',
    description = 'schedule reminder notification',
    long_description = readme,
    long_description_content_type = 'text/x-rst',
    url = 'https://github.com/kenkundert/remind',
    download_url = 'https://github.com/kenkundert/remind/tarball/master',
    license = 'GPLv3+',
    scripts = 'remind'.split(),
    install_requires = 'docopt inform quantiphy arrow'.split(),
    python_requires = '>=3.6',
    zip_safe = True,
    keywords = 'reminder notification schedule'.split(),
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Environment :: Console',
        'Intended Audience :: End Users/Desktop',
        'License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)',
        'Natural Language :: English',
        'Operating System :: POSIX :: Linux',
        'Programming Language :: Python :: 3',
        'Topic :: Utilities',
    ],
)
