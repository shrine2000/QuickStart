from setuptools import setup, find_packages

setup(
    name="quickstart",
    version="0.0.1",
    packages=find_packages(),
    install_requires=[
        "typer[all]",
    ],
    entry_points={
        "console_scripts": [
            "qs = quickstart.cli:app",
        ],
    },
    description="A CLI tool to initialize new projects.",
    author="Shrine Sabu",
    url="https://github.com/shrine2000/QuickStart",
)
