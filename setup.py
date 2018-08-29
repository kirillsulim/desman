from setuptools import setup, find_packages

setup(
    name="desman",
    version="0.1.0",
    author="Kirill Sulim",
    author_email="kirillsulim@gmail.com",
    description="Console HTTP API tool",
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
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ),
)
