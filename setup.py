try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

setup(
    name='libopenttd-python2',
    version='1.0.0',
    author="Steven 'Xaroth' Noorbergen",
    author_email='xaroth@opendune.org',
    packages=['openttd'],
    scripts=['ottd-client.py', 'ottd-gameinfo.py', 'ottd-rcon.py', 'ottd-serverstats.py', 'ottd_client_event.py', 'ottd_config.py'],
    url='https://github.com/ropenttd/libopenttd-python',
    license='https://www.gnu.org/licenses/gpl-3.0.en.html',
    description='A small library for the Client Port interface for OpenTTD.',
    long_description=open('README.md').read(),
    classifiers=[
        'Intended Audience :: Developers',
        'License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Topic :: Games/Entertainment',
        'Topic :: Software Development :: Libraries',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: Utilities',
    ]
)
