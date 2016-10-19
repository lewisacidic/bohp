#! /usr/bin/env python
# -*- coding: utf-8 -*-
#
# Copyright (C) 2016 Rich Lewis <rl403@cam.ac.uk>
# License: MIT

""" Setup the nmr_prediction package. """

from setuptools import setup, find_packages


def metadata():
    """ The metadata for the package. """

    return dict(
        name='bohp',
        maintainer='Rich Lewis',
        maintainer_email='rl403@cam.ac.uk',
        description='A scikit-learn like interface for Bayesian Optimisation '
                    'of hyperparameters',
        license='MIT',
        url='https://github.com/richlewis42/bohp',
        version='0.0.1',
        download_url='https://github.com/richlewis42/bohp/archive/'
                     'master.zip',
        classifiers=[
            'Intended Audience :: Science/Research',
            'Programming Language :: Python',
            'License :: OSI Approved :: MIT License']
    )


def requirements():
    """ The requirements for the package. """

    with open('requirements.txt') as f:
        return [l.strip() for l in f]


def test_requirements():
    """ The test requirements for the package. """

    with open('test_requirements.txt') as f:
        return [l.strip() for l in f]


def long_description():
    """ The long description for the package. """

    with open('README.md') as f:
        return f.read()


def setup_package():
    """ Set up the package. """

    setup(
        packages=find_packages(exclude=['test']),
        install_requires=requirements(),
        tests_require=test_requirements(),
        long_description=long_description(),
        **metadata()
    )


if __name__ == '__main__':
    setup_package()
