import os
from distutils.core import setup

setup(
    name="aws-actions",
    install_requires=['botocore'],
    entry_points={
      "console_scripts": [
          "aws-actions = actions:main"
        ]
    }
)
