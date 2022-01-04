import os
from setuptools import find_packages, setup
from esi import __version__

this_directory = os.path.abspath(os.path.dirname(__file__))
with open(os.path.join(this_directory, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

setup(
    name='pathfinder',
    version=__version__,
    packages=find_packages(),
    include_package_data=True,
    license='MIT',
    description='Alliance Auth Serrvice module for Pathfinder',
    long_description=long_description,
    long_description_content_type='text/markdown',
    author='ak',
    author_email='',
    classifiers=[
        'Environment :: Web Environment',
        'Framework :: Django',        
        'Framework :: Django :: 2.2',
        'Intended Audience :: Developers',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
    ],
)
