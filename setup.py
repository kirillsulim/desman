from setuptools import setup, find_packages
from os import path


project_directory = path.abspath(path.dirname(__file__))

def load_from(file_name):
    with open(path.join(project_directory, file_name), encoding='utf-8') as f:
        return f.read()

setup(
    name='desman',
    version=load_from('desman.version').strip(),
    url='https://github.com/kirillsulim/desman',
    author='Kirill Sulim',
    author_email='kirillsulim@gmail.com',
    description='Console HTTP API tool',
    long_description=load_from('README.md'),
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
        'Development Status :: 4 - Beta',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'License :: OSI Approved :: MIT License',
        'Topic :: Internet :: WWW/HTTP',
        'Operating System :: OS Independent',
    ),
)
