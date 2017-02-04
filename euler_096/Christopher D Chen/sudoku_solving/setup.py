from setuptools import setup

long_description = """Sudoku solving library with SudokuBoard object that has useful methods for backtracking."""

setup(
    name='sudoku_solving',
    author='Christopher Chen',
    author_email='christopher.chen1995@gmail.com',
    version='0.1.0',
    description="""A sudoku solving library utilizing board optimization and backtracking.""",
    long_description=long_description,
    classifiers=[
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.3",
        "Programming Language :: Python :: 3.4",
        "Programming Language :: Python :: 3.5",
        "Operating System :: OS Independent",
    ],
    keywords="",
    url='',
    license='Public Domain',
    packages=['sudoku_solving'],
    download_url="",
    scripts=["bin/sudoku_solving"],

    install_requires=[],
    zip_safe=True
)
