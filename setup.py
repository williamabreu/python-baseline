# Usage:
#
# -- Build the project for distribution:
#   python3 setup.py sdist bdist_wheel
#
# -- Run unit tests:
#   python3 setup.py test

import setuptools

# FIXME: Do change the 'project_name' here to the correct one.
from project_name import __name__, __version__

setuptools.setup(
    name=__name__,
    version=__version__,
    license="MIT License",
    author="William Abreu",
    author_email="contato@williamabreu.net",
    description="Summarize your project purpose here",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/williamabreu/python-baseline",
    install_requires=open("requirements.txt").read().splitlines(),
    platforms="any",
    packages=setuptools.find_packages(".", exclude=(f"{__name__}.tests",)),
    python_requires=">=3.8",
    test_suite=f"{__name__}.tests",
    keywords="",
    entry_points={"console_scripts": [f"{__name__}={__name__}.__main__:main"]},
    classifiers=[
        "Environment :: Console",
        "Programming Language :: Python :: 3 :: Only",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Topic :: Utilities",
    ],
)
