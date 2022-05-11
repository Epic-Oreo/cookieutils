from cookieutils import get_version 
try: # for pip >= 10
    from pip._internal.req import parse_requirements
except ImportError: # for pip <= 9.0.3
    from pip.req import parse_requirements
from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

requirements = parse_requirements('requirements.txt', session=False)
install_requires = [str(r.req) for r in requirements]

setup(
    name             = 'cookieutils-epicoreo',
    description      = 'A ton of usefull utils for python console applications',
    packages         =  find_packages(),
    author           = 'Epic Oreo',
    author_email     = 'None',
    install_requires = install_requires,
    version          = get_version(),
    zip_safe         = False,
    keywords         = "cookieutils",
    long_description = long_description,
    long_description_content_type="text/markdown",
    classifiers      = [
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GPL-3.0-only",
        "Operating System :: OS Independent",
                      ]
)