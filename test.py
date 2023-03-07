import pytest
import sqlite3
from project0 import fetchIncidents, extractIncidents, createDb, populateDb, status

url = "https://www.normanok.gov/sites/default/files/documents/2023-02/2023-02-22_daily_incident_summary.pdf"

def testFetchIncidents():
    testSet = fetchIncidents.fetchIncidents(url)
    assert True

def testExtractIncidents():
    test = extractIncidents.extractIncidents('incidents.pdf')
    assert True

def testCreateDb():
    testdb = createDb.createDb()
    assert True

def testPopulateDb():
    test = extractIncidents.extractIncidents('incidents.pdf')
    testdb = createDb.createDb()
    populateDb.populateDb(testdb, test)
    assert True

def status():
    test = extractIncidents.extractIncidents('incidents.pdf')
    testdb = createDb.createDb()
    populateDb.populateDb('incidents.db', test)
    status.status('incidents.db')
    assert True
