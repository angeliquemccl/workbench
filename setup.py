import setuptools

# read the description file 
from os import path
this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, 'doc/description.md'), encoding='utf-8') as f:
    long_description = f.read()

setuptools.setup(
    name="cinemasci",
    version="2.0.0",
    author="David H. Rogers",
    author_email="dhr@lanl.gov",
    description="Cinema scientific toolset.",
    long_description=long_description,
    long_description_content_type='text/markdown',
    url="https://github.com/cinemascience",
    include_package_data=True,
    packages=["cinemasci" 
            ],
    install_requires=[
        "wheel",
        "pyyaml",
        "matplotlib"
    ],
    scripts=[''],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: BSD License",
        "Operating System :: OS Independent",
    ],
)