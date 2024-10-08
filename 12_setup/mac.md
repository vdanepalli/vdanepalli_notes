# General Setup on MacOS


```python
# Installing pyodbc on mac silicon chip
pip uninstall pyodbc
brew install unixodbc

export CPPFLAGS="-I/opt/homebrew/Cellar/unixodbc/2.3.12/include"
export LDFLAGS="-L/opt/homebrew/Cellar/unixodbc/2.3.12/lib -liodbc -liodbcinst"

cd path/to/pyodbc-4.0.32.tar.gz
pip install pyodbc-4.0.32.tar.gz

https://whodeenie.medium.com/installing-pyodbc-and-unixodbc-for-apple-silicon-8e238ed7f216
```

<br/>
<br/>

```python
# Add custom packages to sys.path for each jupyter session
export PYTHONPATH="$PYTHONPATH:/Users/vd/Desktop/CC/_desktop/code/"

nano ~/.ipython/profile_default/startup/startup.py

import sys
sys.path.append('/Users/vd/Desktop/CC/_desktop/code/')
```

<br/>
<br/>

