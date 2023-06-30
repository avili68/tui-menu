from setuptools import setup

setup(
    name="tui-menu",
    version="0.1.0",
    description="A module for TUI Menu driven application",
    url="https://github.com/avili68/tui-menu",
    author="Avi Liani",
    author_email="avi@liani.co.il",
    license="GPL",
    packages=["tui-menu"],
    install_requires=["console>=0.9907"],
    python_requires=">=3",
    classifiers=[
        "Development Status :: 4 - Beta",
        "Environment :: Console",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)",
        "Natural Language :: English",
        "Operating System :: MacOS",
        "Operating System :: POSIX :: Linux",
        "Programming Language :: Python :: 3",
        "Topic :: Software Development",
        "Topic :: Software Development :: User Interfaces",
    ],
)
