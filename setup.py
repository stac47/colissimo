from setuptools import setup

VERSION = '0.3'

setup(
    name='colissimo',
    version=VERSION,
    py_modules=['colissimo'],
    description='Follow you Colissimo parcels from your shell',
    author='Laurent Stacul',
    author_email='laurent.stacul@gmail.com',
    url='https://github.com/stac47/colissimo',
    download_url='https://github.com/stac47/colissimo/archive/{}.tar.gz'.format(VERSION),
    keywords=['parcel', 'tool', 'La Poste'],
    classifiers=[],
    install_requires=[
        'requests',
        'click',
        'terminaltables',
        'colorclass',
    ],
    entry_points='''
        [console_scripts]
        colissimo=colissimo:cli
    ''',
)
