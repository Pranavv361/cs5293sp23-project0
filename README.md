# Author - Pranav Vichare
# Project - Norman Police Department Incident Summary
# About

```python
import argparse
import pytest
import PyPDF2
import re
import sqlite3
import urllib.request
```
To run the code, Import all the libraries listed above.

```python
```

Assumptions:
1. Nature of Incidents field contains values which are of Start Case, Title Case, camelCase, sentence case etc.

Bugs:   
1. If the Nature of Incident field starts with a word  in ALL CAPS, then the word will be concatenated to th Address field.
   
