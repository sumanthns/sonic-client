from setuptools import setup, find_packages
from pip.req import parse_requirements

install_reqs = parse_requirements('requirements.txt', session=False)
reqs = [str(ir.req) for ir in install_reqs]

setup(name='sonic_client',
      version='0.1',
      description='client to be installed on raspberry pis connected with sonic',
      url='https://github.com/sumanthns/sonic_client.git',
      author='Sumanth Nagadavalli Suresh',
      author_email='nsready@gmail.com',
      license='MIT',
      packages=find_packages(),
      install_requires=reqs,
      entry_points= {
          'console_scripts': ['sonic-client=bin.sonic:main'],
      },
      zip_safe=False)