# Usage:
#
# -- Build the project for distribution:
#   python3 setup.py sdist bdist_wheel
#
# -- Run unit tests:
#   python3 setup.py test

import setuptools

# FIXME: Do change the 'project_name' here to the correct one.
import project_name as src

setuptools.setup(
    name=src.__name__,
    version=src.__version__,
    license="MIT License",
    author="William Abreu",
    author_email="contato@williamabreu.net",
    description="Summarize your project purpose here",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/williamabreu/python-baseline",
    install_requires=open("requirements.txt").read().splitlines(),
    platforms="any",
    packages=setuptools.find_packages(".", exclude=(f"{src.__name__}.tests",)),
    python_requires=">=3.8",
    test_suite=f"{src.__name__}.tests",
    keywords="",
    entry_points={
        "console_scripts": [f"{src.__name__}={src.__name__}.__main__:main"]
    },
    classifiers=[
        "Environment :: Console",
        "Programming Language :: Python :: 3 :: Only",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Topic :: Utilities",
    ],
)
