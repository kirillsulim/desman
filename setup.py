from setuptools import setup, find_packages
from os import path


project_directory = path.abspath(path.dirname(__file__))
with open(path.join(project_directory, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='desman',
    version="1.0.0",
    url='https://github.com/kirillsulim/desman',
    author='Kirill Sulim',
    author_email='kirillsulim@gmail.com',
    description='Console HTTP API tool',
    long_description=long_description,
    long_description_content_type='text/markdown',
    packages=find_packages(where='src'),
    package_dir={'': 'src'},
    entry_points={
        'console_scripts': [
            'desman = desman.desman:main',
        ]
    },
    install_requires=[
        'requests >= 2.19.1',
        'pyyaml >= 3.13',
        'Jinja2 >= 2.10'
    ],
    classifiers=(
        'Environment :: Console',
        'Intended Audience :: Developers',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'License :: OSI Approved :: MIT License',
        'Topic :: Internet :: WWW/HTTP',
        'Operating System :: OS Independent',
    ),
)
