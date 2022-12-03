import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="expbuddy",
    version="0.0.1",
    author="yohpaulkevin@gmail.com",
    author_email="",
    description="",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
    ],
    entry_points={
        "console_scripts" : ["sat = src.main:app"]
    },
    setup_requires=["numpy"],
    install_requires=[
        "Cython==0.29.24",
        "numpy==1.22.0",
        "jupyterlab==3.1.11",
        "matplotlib==3.4.2",
        "pandas==1.3.3",
        "pydantic==1.8.2",
        "scikit-learn==0.24.2",
        "seaborn==0.11.1",
        "statsmodels==0.12.2",
        "typer==0.3.2",
        "pyarrow==3.0.0",
    ],
    python_requires=">=3.7",
)
