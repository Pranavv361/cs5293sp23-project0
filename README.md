## Author - Pranav Vichare
## Project - Norman Police Department Incident Summary
**About:**  In this project, we access Norman Police Department Database online and download the files which contains summary of Incidents in the form of PDF file. We then extract the text from the pdf and ingest all the records in the database by creating a table which will store all 5 fields in the database - Data/Time, Incident No, Location, Nature, Incident ORI

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
def main(url):
    # Download data
    incident_data = fetchIncidents.fetchIncidents(url)
    
    #Extract data
    incidents = extractIncidents.extractIncidents('incidents.pdf')
	
    # Create new database
    createDb.createDb()
	
    # Insert data
    populateDb.populateDb('incidents.db', incidents)
	
    # Print incident counts
    status.status('incidents.db')

#To call main function from the terminal
if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("--incidents", type=str, required=True, 
                         help="Incident summary url.")
     
    args = parser.parse_args()
    #print(args)
    if args.incidents:
        main(args.incidents)
```
The main function mentioned above will be executed and calls other functions. The url input from the user will be processed from the command terminal and later other functions will be called.
```python
fetchIncidents.fetchIncidents(url)
```
The url will be sent to **fetchIncidents.fetchIncidents(url)** fetchIncidents function in fetchIncidents.py file which we download the pdf file using urllib library.
The download file *incidents.pdf* is then stored in the local directory.
```python
extractIncidents.extractIncidents('incidents.pdf')
```
The above function will extract the text using regular expression Library and store it in form a list of tuples which has all the 5 fields to required.
```python
createDb.createDb()
populateDb.populateDb('incidents.db', incidents)
```
The above code will create an empty database with a table with 5 columns, column for each field and then populate the extract from pdf to the database.
```python
status.status('incidents.db')
```
Using status method to print all the values in the nature field with their count. Using **Select** and **Groupby** command to get the count of the incidents.


### Assumptions:
1. Nature of Incidents field contains values which are of type Start Case, Title Case, camelCase, sentence case etc. Incidents fields does not start with ALL CAPS word.
2. The Location field is a single line field.

### Bugs:   
1. If the Nature of Incident field starts with a word in ALL CAPS, then the word will be concatenated to the Address field.
   
