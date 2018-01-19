from setuptools import setup


setup(
    name='colissimo',
    version='0.1',
    py_modules=['colissimo'],
    install_requires=[
        'Click',
        'Requests',
        'Colorama',
    ],
    entry_points='''
        [console_scripts]
        colissimo=colissimo:cli
    ''',
)
