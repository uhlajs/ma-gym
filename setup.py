
# -*- coding: utf-8 -*-

# DO NOT EDIT THIS FILE!
# This file has been autogenerated by dephell <3
# https://github.com/dephell/dephell

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup


import os.path

readme = ''
here = os.path.abspath(os.path.dirname(__file__))
readme_path = os.path.join(here, 'README.rst')
if os.path.exists(readme_path):
    with open(readme_path, 'rb') as stream:
        readme = stream.read().decode('utf8')


setup(
    long_description=readme,
    name='ma-gym',
    version='0.0.1',
    description='A collection of multi agent environments based on OpenAI gym.',
    python_requires='==3.*,>=3.8.0',
    project_urls={"repository": "https://gitlab.com/uhlajs/ma-gym"},
    author='Anurag Koul',
    author_email='koulanurag@gmail.com',
    license='Apache License 2.0',
    keywords='Reinforcement Learning Multiagent Systems Deep Learning',
    packages=['ma_gym', 'ma_gym.envs', 'ma_gym.envs.checkers', 'ma_gym.envs.combat', 'ma_gym.envs.openai', 'ma_gym.envs.pong_duel',
              'ma_gym.envs.predator_prey', 'ma_gym.envs.switch', 'ma_gym.envs.traffic_junction', 'ma_gym.envs.utils', 'ma_gym.wrappers', 'ma_gym.wrappers.monitoring'],
    package_dir={"": "."},
    package_data={},
    install_requires=['gym==0.*,>=0.17.2', 'numpy==1.*,>=1.19.1',
                      'pillow==7.*,>=7.2.0', 'scipy==1.*,>=1.5.2'],
    extras_require={"dev": ["autopep8", "dephell==0.*,>=0.8.3", "flake8", "imageio==2.*,>=2.9.0", "ipdb",
                            "ipykernel", "ipython", "jedi", "pylint", "pytest==6.*,>=6.0.1", "pytest-cases==2.*,>=2.2.2", "rope"]},
)
