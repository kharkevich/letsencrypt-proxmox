import os
from setuptools import setup

version = '0.1.0'

install_requires = [
    'letsencrypt',
    'zope.interface',
]

def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name='letsencrypt-proxmox',
    version=version,
    author="Aliaksandr Kharkevich",
    author_email='aliaksandr_kharkevich@outlook.com',
    description="Proxmox VE plugin for Let's Encrypt client",
    license='Apache License 2.0',
    keywords = ['letsencrypt', 'proxmox'],
    url='https://github.com/kharkevich/letsencrypt-proxmox',
    download_url = 'https://github.com/kharkevich/letsencrypt-proxmox/archive/'+version+'.tar.gz',
    packages=['proxmox_plugin'],
    long_description=read('README.md'),
    include_package_data=True,
    install_requires=install_requires,
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Topic :: Utilities",
        "License :: OSI Approved :: Apache Software License",
    ],
    platforms='any',
    entry_points={
        'letsencrypt.plugins': [
            'proxmox = proxmox_plugin.proxmox:ProxmoxInstaller',
        ],
    },
)
