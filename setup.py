from setuptools import setup, find_packages

setup(
    name="Batman",
    version="0.1",
    packages=find_packages(where='src'),
    package_dir={'': 'src'},
    entry_points={
        'console_scripts': [
            'batman = batman.batman:main',
        ]
    },
    install_requires=[
        'requests >= 2.19.1',
        'pyyaml >= 3.13',
    ],
)
