import PyPDF2
import re

# The below function will extract the text from the download pdf file
def extractIncidents(path):
    with open(path, 'rb') as f:
        pdf_reader = PyPDF2.PdfReader(f)
        #print("Reading Text in the pdf")
        text = ""
        #reading each page and saving it in text
        for page in range(len(pdf_reader.pages)):
            page_obj = pdf_reader.pages[page]
            text += page_obj.extract_text()
        # Adding new line at the start of new page to avoid concatenation of entries
            if page >= 0:
                text+= "\n"
    #To remove column headers
    text = re.sub(
            'Date / Time Incident Number Location Nature Incident ORI\n',
            '',
            text)
    # To remove PDF heading
    text = re.sub(
            r'NORMAN POLICE DEPARTMENT\nDaily Incident Summary \(Public\)',
            '',
            text)
    
    # To add special character ! at start of each line before datetime
    text = re.sub(
            r'(\d{1,2}/\d{1,2}/\d{4}\s\d{1,2}:\d{2})'
            ,lambda x: f'!{x.group(1)}',
            text)
    
    # To bring multiple lines address on same line
    text = re.sub(
            r'([\w,\.;#\'<>&\(\) /-]*) \n([\w,\.;#\'<>&\(\) /-]*)',
            lambda x: f'{x.group(1)} {x.group(2)}',
            text)
    # To add special character '!' at the end of last page
    text += '!'
    etext = []
    # To find all the records matching this pattern and dividing the records into list
    # Date/Time , Incident number, Location, Nature, Incident ORI
    etext = re.findall (
            r'(\d{1,2}/\d{1,2}/\d{4}\s\d{1,2}:\d{2})\s(\d{4}-\d{8})\s([A-Z0-9,\.;#\'<>&\(\) /-]*)\s([\w /]*)\s(\w+)',
            text)
    # To find all the blank inputs 
    etext += re.findall(
            r'(\d+/\d+/\d{4}.\d+:\d\d)\n(\d{4}-\d{8})()()\n([\w /]*)\n;;',
            text)

    #return extracted text
    return etext




