import argparse
import fetchIncidents, extractIncidents, createDb, populateDb, status

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

# To test out the function without terminal inputs(directly running the code)
# if __name__ == '__main__':
#     main(url = "https://www.normanok.gov/sites/default/files/documents/2023-02/2023-02-22_daily_incident_summary.pdf")