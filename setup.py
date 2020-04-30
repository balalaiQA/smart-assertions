import io
import os

from setuptools import setup


setup(
    name='smart-assertions',
    version='1.0.2',
    description='Soft assertions for Python',
    long_description=io.open(os.path.join(os.path.dirname('__file__'), 'README.md'), encoding='utf-8').read(),
    long_description_content_type='text/markdown',
    author='balalaiQA',
    url='https://github.com/balalaiQA/smart-assertions',
    packages=['smart_assertions']
)
