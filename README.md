[![Build status](https://ci.appveyor.com/api/projects/status/qt40clxeegnqi6ex?svg=true)](https://ci.appveyor.com/project/excitoon/tempfile2)

# `tempfile2`

`tempfile` wrapper with slightly more convenient interface.

## Install

```
pip install tempfile2
```

## Usage

```python
import tempfile2

with tempfile2.NamedTemporaryFile(close=True) as temp_file:
    # Closed at this point
    # ...
# Deleted at this point
```

## Build

```
python3 setup.py bdist_wheel --universal
```
