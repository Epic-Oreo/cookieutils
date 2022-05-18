import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="cookieutils-epicoreo",
    version="0.0.2",
    author="Epic Oreo",
    author_email="author@example.com",
    description="A ton of usefull utils for python console applications",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Epic-Oreo/cookieutils",
    project_urls={
        "Bug Tracker": "https://github.com/Epic-Oreo/cookieutils/issues",
    },
    classifiers = [
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
    python_requires=">=3.6",
)