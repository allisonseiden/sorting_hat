import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="sorting_hat",
    version="0.0.1",
    author="Allison Seiden",
    author_email="ahseiden@gmail.com",
    description="Sorts indels into mutational classes",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/allisonseiden/sorting_hat",
    packages=setuptools.find_packages(),
    classifiers=(
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ),
    entry_points={
        "console_scripts": ['sorting_hat=sorting_hat.sorting_hat:main']
        },
    install_requires=[
          'pandas', 'numpy'
    ],
    python_requires='>=3',
)
