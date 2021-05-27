import pathlib
from setuptools import setup
from pyscraper_ml import __version__

# The directory containing this file
HERE = pathlib.Path(__file__).parent

# The text of the README file
README = (HERE / "README.md").read_text()

# This call to setup() does all the work
setup(
    name="pyscraper_ml",
    description="A general purpose webscraper",
    long_description=README,
    long_description_content_type="text/markdown",
    url="https://github.com/EricSchles/pyscraper_ml",
    author="Eric Schles",
    version=__version__,
    author_email="ericschles@gmail.com",
    license="MIT",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
    ],
    packages=["pyscraper_ml", 'pyscraper_ml.scrapers'],
    include_package_data=True,
    install_requires=[
        "selenium", "requests", "lxml",
    ],
)
