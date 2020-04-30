import io
import os

from setuptools import setup


setup(
    name='smart-assertions',
    version='1.0.1',
    description='Soft assertions for Python',
    long_description=io.open(os.path.join(os.path.dirname('__file__'), 'README.md'), encoding='utf-8').read(),
    author='balalaiQA',
    url='https://github.com/balalaiQA/smart-assertions',
    packages=['smart_assertions']
)
