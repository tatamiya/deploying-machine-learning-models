# PYTHONPATH settings
To solve the module path problem in executing pytest,
PYTHONPATH should be configured:
```
export PYTHONPATH="$(pwd):$PYTHONPATH"
```

# Packaging
```
pip install -e .
```

When packaging again after directory restructuring, 
you first have to delete the symbolic link to the previous one:
```
rm ~/.pyenv/versions/X.X.X/envs/<env name>/lib/pythonX.X/site-packages/regression-model.egg-link
```