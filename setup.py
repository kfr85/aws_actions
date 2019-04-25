import os
from distutils.core import setup

setup(name='aws_actions',
      version='0.0.1',
      description='Listing Aws Actions from boto/botocore',
      long_description=readme,
      author='',
      author_email='',
      url='',
      install_requires=['botocore'],
      license=license,
      packages=find_packages(exclude=('tests', 'docs'))
      )
