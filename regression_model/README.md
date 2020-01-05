# PYTHONPATH settings
To solve the module path problem in executing pytest,
PYTHONPATH should be configured:
```
export PYTHONPATH="$(pwd):$PYTHONPATH"
```