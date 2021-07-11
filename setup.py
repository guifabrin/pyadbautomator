import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="pyadbautomator",
    version="0.0.8",
    author="Guilherme Fabrin Franco",
    author_email="guilherme.fabrin@gmail.com",
    description="PyAdbAutomator is a Python library for automating some android tasks using ADB interface",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/guifabrin/pyadbautomator",
    project_urls={
        "Bug Tracker": "https://github.com/guifabrin/pyadbautomator/issues",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
    python_requires=">=3.6",
)