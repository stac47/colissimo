from setuptools import setup
from pip.req import parse_requirements
import pip.download


install_reqs = parse_requirements('requirements.txt',
                                  session=pip.download.PipSession())
reqs = [str(ir.req) for ir in install_reqs]

setup(
    name='colissimo',
    version='0.2',
    py_modules=['colissimo'],
    install_requires=reqs,
    entry_points='''
        [console_scripts]
        colissimo=colissimo:cli
    ''',
)
