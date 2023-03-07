import argparse
import fetchIncidents, extractIncidents, createDb, populateDb, status

def main(url):
    # Download data
    incident_data = fetchIncidents.fetchIncidents(url)
    
    #Extract data
    incidents = extractIncidents.extractIncidents('incidents.pdf')
    #print(incidents[361])
	
    # Create new database
    createDb.createDb()
	
    # Insert data
    populateDb.populateDb('incidents.db', incidents)
	
    # Print incident counts
    status.status('incidents.db')

#to call main function from the terminal
if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("--incidents", type=str, required=True, 
                         help="Incident summary url.")
     
    args = parser.parse_args()
    #print(args)
    if args.incidents:
        main(args.incidents)

# if __name__ == '__main__':
#     main()