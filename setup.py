from setuptools import setup, find_packages

setup(
    name='desman',
    version="0.1.1",
    url='https://github.com/kirillsulim/desman',
    author='Kirill Sulim',
    author_email='kirillsulim@gmail.com',
    description='Console HTTP API tool',
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
