import pytest
import sqlite3

#Importing files from project0 folder
from project0 import fetchIncidents, extractIncidents, createDb, populateDb,status

#Using below URL for test
url = "https://www.normanok.gov/sites/default/files/documents/2023-02/2023-02-22_daily_incident_summary.pdf"

#creating testFetchIncidents method
def testFetchIncidents():
    testSet = fetchIncidents.fetchIncidents(url)
    assert True

#creating testExtractIncidents method
def testExtractIncidents():
    test = extractIncidents.extractIncidents('incidents.pdf')
    assert True

#creating testCreateDb method to test creation of the database
def testCreateDb():
    testdb = createDb.createDb()
    assert True

#creating testPopulateDb method
def testPopulateDb():
    test = extractIncidents.extractIncidents('incidents.pdf')
    testdb = createDb.createDb()
    populateDb.populateDb(testdb, test)
    assert True

#creating teststatus method
def teststatus():
    test = extractIncidents.extractIncidents('incidents.pdf')
    testdb = createDb.createDb()
    populateDb.populateDb('incidents.db', test)
    status.status('incidents.db')
    assert True
