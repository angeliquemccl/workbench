# This workflow will install Python dependencies, run tests and lint with a single version of Python
# For more information see: https://help.github.com/actions/language-and-framework-guides/using-python-with-github-actions

name: CinemaSmokeTest

on:
  push:

jobs:
  build:

    runs-on: ubuntu-latest
    strategy:
      matrix:
        python-version: [3.7, 3.8, 3.9]

    steps:
    - uses: actions/checkout@v2
    - name: Set up Python ${{ matrix.python-version }} 
      uses: actions/setup-python@v2
      with:
        python-version: ${{ matrix.python-version }} 
    - name: Install dependencies
      run: |
        python setup.py install
    - name: Run the tests 
      run: |
        python -m unittest testing/CinemaSmokeTest.py
