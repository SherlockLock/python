# Setting up and working with environment variables with Python

## local environment

```python
import os
```

contains all information about the environment python is running in


## .evn

You can also work with .env files within your workspace to hold all your secrets.

It is typical to have two sets of .env files: dev and prod

These files will contain secrets used throughout your code.

### Create

1. Install the dotenv package

```bash
pip install python-dotenv
```

2. Create a new file with your preferred method and label the extension as .env

NOTE: Make sure to include this file in the .gitignore file, so no one else can see it!

3. Add your variables

``` 
SOME_KEY=123abc
user_password=password
```

### Usage

To load the variables, ensure you run the following before trying to access the variables throughout your code.

```python
from dotenv import load_dotenv
load_dotenv()
```

Which will look in the current directory to find your environment file. If it does not find it, it will move up your directory tree until it finds one.

You can also pass a path to the function to specify where to find the file.


To access these variables throughout your code simply add the following to the top of the file you are accessing code from

```python
from dotenv import dotenv_values
dotenv_values().get('SOME_KEY')
```





