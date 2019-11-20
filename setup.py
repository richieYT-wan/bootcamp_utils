import setuptools

with open("README.md", "r") as f:
    long_description = f.read()

setuptools.setup(
    name='rw_bootcamp',
    version='0.0.1',
    author='Richie Wan',
    author_email='richie.wan@epfl.ch',
    description='Utilities for use in bootcamp.',
    long_description=long_description,
    long_description_content_type='ext/markdown',
    packages=setuptools.find_packages(),
    classifiers=(
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ),
)