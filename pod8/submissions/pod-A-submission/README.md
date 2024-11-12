<div align="center">
    <h1>Pod A Markdown Submission</h1>
    <h2>Testing Tools</h2>
</div>

## Getting Started

Quick start guide for pytest

### Requirements
1. python version 3.8 or higher
- windows: `$ choco install python`
- mac: `$ brew install python`
- linux(debian): `$ sudo apt install python3`
2. install pip
- windows: `$ py -m ensurepip --upgrade`
- mac: `$ python -m ensurepip --upgrade`
- linux: `$ python -m ensurepip --upgrade`
3. install pytest
```sh
$ pip install -U pytest
```

## Usage

Guide on how to use pytest

### Code
1. Starter Code
```
# content of test_sample.py
def func(x):
    return x + 1


def test_answer():
    assert func(3) == 5
```
2. Run Code
```sh
$ pytest
```
