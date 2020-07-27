# Usage: 
#
# -- Build the project for distribution:
#   python3 setup.py sdist bdist_wheel
# 
# -- Run unit tests:
#   python3 setup.py test


import setuptools

# Change the 'project_name' here to the correct one.
from project_name import __version__

# Set the project name here.
PROJECT_NAME = 'project_name'

setuptools.setup(
    name=PROJECT_NAME,
    version=__version__,
    license='MIT License',
    author='William Abreu',
    author_email='contato@williamabreu.net',
    description='Summarize your project purpose here',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/williamabreu/python-baseline',
    install_requires=open('requirements.txt').read().splitlines(),
    platforms='any',
    packages=setuptools.find_packages('.', exclude=(f'{PROJECT_NAME}.tests',)),
    python_requires='>=3.7',
    test_suite=f'{PROJECT_NAME}.tests',
    keywords='',
    entry_points={
        'console_scripts': [
            f'{PROJECT_NAME}={PROJECT_NAME}.__main__:main'
        ]
    },
    classifiers=[
        'Environment :: Console',
        'Programming Language :: Python :: 3 :: Only',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: Utilities',
    ],
)
