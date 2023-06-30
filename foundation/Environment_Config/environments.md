# What are python environments

When working with python, it is best to create local workspaces that contain all of the packages python will need for the specific tasks. 

This is to prevent dependency issues from arising when working on seperate projects or tasks. 

There are two types of local environments:
1. Virtual Environments 
2. Conda Environments


## Creating Virtual Environments (MacOS)

``` bash
python3 -m venv /path/to/new/virtual/environment
```

OR

```bash
python3 -m venv .venv
```

Refer to https://docs.python.org/3/library/venv.html for more info