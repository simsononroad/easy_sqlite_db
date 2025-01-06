from setuptools import setup, find_packages
import codecs
import os
VERSION = '1.1'
DESCRIPTION = 'An easy database package'
LONG_DESCRIPTION = 'A package that based on sqlite'

# Setting up
setup(
    name="easy_sqlite_db",
    version=VERSION,
    author="Simson_on_the_road",
    description=DESCRIPTION,
    long_description_content_type="text/markdown",
    long_description=LONG_DESCRIPTION,
    packages=find_packages(),
    install_requires=['sqlite3'],
    keywords=['python', 'easy', 'db', 'database', 'easydb'],
    classifiers=[
        "Development Status :: 1 - Planning",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ]
)