from setuptools import setup, find_packages
from os import path

here = path.abspath(path.dirname(__file__))

long_description = """"
DataJoint interactive tutorials with examples from electrophysiology and calcium-imaging
"""

with open(path.join(here, "requirements.txt")) as f:
    requirements = f.read().splitlines()

setup(
    name="datajoint-tutorials",
    version="0.1.3",
    description="DataJoint interactive tutorials",
    long_description=long_description,
    author="DataJoint",
    author_email="support@datajoint.com",
    license="MIT",
    url="https://github.com/datajoint/datajoint-tutorials",
    keywords="neuroscience datajoint",
    packages=find_packages(exclude=["contrib", "docs", "tests*"]),
    install_requires=requirements,
)
