import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="pygenerator_c_project",
    version="1.0.0",
    author="Ericson Joseph",
    author_email="ericsonjoseph@gmail.com",
    description="Generator C Project",
    long_description=long_description,
    long_description_content_type="text/markdown",
    scripts = [],
    url="https://github.com/ericsonj/pygenerator_c_project",
    license="MIT",
    packages=setuptools.find_packages(),
    package_data={'': ['*.glade', '*.tar.gz']},
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
