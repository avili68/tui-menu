import codecs
import os.path
from setuptools import setup


def read(rel_path):
    here = os.path.abspath(os.path.dirname(__file__))
    with codecs.open(os.path.join(here, rel_path), "r") as fp:
        return fp.read()


def get_version(rel_path):
    for line in read(rel_path).splitlines():
        if line.startswith("__version__"):
            delim = '"' if '"' in line else "'"
            return line.split(delim)[1]
    else:
        raise RuntimeError("Unable to find version string.")


setup(
    name="tui-menu",
    version=get_version("tui-menu/__init__.py"),
    description="A module for TUI Menu driven application",
    url="https://github.com/avili68/tui-menu",
    author="Avi Liani",
    author_email="avi@liani.co.il",
    license="GPL",
    packages=["tui-menu"],
    install_requires=["console>=0.9907", "ezenv>=0.92"],
    python_requires=">=3",
    classifiers=[
        "Development Status :: 4 - Beta",
        "Environment :: Console",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)",
        "Natural Language :: English",
        "Operating System :: MacOS",
        "Operating System :: POSIX :: Linux",
        "Programming Language :: Python :: 3.9",
        "Topic :: Software Development",
        "Topic :: Software Development :: User Interfaces",
    ],
)
