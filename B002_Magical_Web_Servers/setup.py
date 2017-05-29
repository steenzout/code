#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pip.download

from pip.req import parse_requirements

from setuptools import find_packages, setup


def requirements(requirements_file):
    """Return packages mentioned in the given file.

    Args:
        requirements_file (str): path to the requirements file to be parsed.

    Returns:
        (list): 3rd-party package dependencies contained in the file.
    """
    return [
        str(pkg.req) for pkg in parse_requirements(
            requirements_file, session=pip.download.PipSession()) if pkg.req is not None]


setup(name='B002_Magical_Web_Servers',
      version='1.0.0',
      description='Exercise to build a simple web service.',
      author='Skyler Lewis',
      author_email='sblnog@gmail.com',
      classifiers=[
          'Development Status :: 5 - Production/Stable',
          'Intended Audience :: Developers',
          'Natural Language :: English',
          'License :: OSI Approved :: Apache Software License',
          'Programming Language :: Python',
          'Programming Language :: Python :: 3',
          'Programming Language :: Python :: 3.6',
      ],
      url='https://github.com/PythonAtThePoint/code/tree/master/B002_Magical_Web_Servers',
      package_dir={'B002_Magical_Web_Servers': '.'},
      install_requires=requirements('requirements.txt'),
      tests_require=requirements('requirements-test.txt'))
