from setuptools import setup, find_packages

with open("README.MD", "r") as readme_file:
    readme = readme_file.read()

requirements = ["ipython>=6", "nbformat>=4", "nbconvert>=5", "requests>=2"]

setup(
    name="notebookconvert",
    version="0.0.1",
    author="Fizioh",
    author_email="contact@yassine-benosmane.fr",
    description="This package convert a Jupyter notebook file into a PDF file",
    url="https://github.com/PyPwheel/NoteBookConvert",
    packages=find_packages(),
    install_requires=requirements,
    classifiers=[
        "Programming language :: Python :: 3.9",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
    ],
)