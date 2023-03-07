import PyPDF2
import re

def extractIncidents(path):
    with open(path, 'rb') as f:
        pdf_reader = PyPDF2.PdfReader(f)
        print("Reading Text in the pdf")
        text = ""
        for page in range(len(pdf_reader.pages)):
            page_obj = pdf_reader.pages[page]
            text += page_obj.extract_text()

            if page >= 0:
                text+= "\n"
    
    text = re.sub(
            'Date / Time Incident Number Location Nature Incident ORI\n',
            '',
            text)
    
    text = re.sub(
            r'NORMAN POLICE DEPARTMENT\nDaily Incident Summary \(Public\)',
            '',
            text)
    
    text = re.sub(
            r'(\d{1,2}/\d{1,2}/\d{4}\s\d{1,2}:\d{2})'
            ,lambda x: f';;{x.group(1)}',
            text)
    
    text = re.sub(
            r'([\w,\.;#\'<>&\(\) /-]*) \n([\w,\.;#\'<>&\(\) /-]*)',
            lambda x: f'{x.group(1)} {x.group(2)}',
            text)
    text += ';;'
    etext = []
    etext = re.findall (
            r'(\d{1,2}/\d{1,2}/\d{4}\s\d{1,2}:\d{2})\s(\d{4}-\d{8})\s([A-Z0-9,\.;#\'<>&\(\) /-]*)\s([\w /]*)\s(\w+)',
            text)
    # etext = re.findall(
    #         r'(\d+/\d+/\d{4}.\d+:\d\d)\n(\d{4}-\d{8})\n([\w,\.;#\'<>&\(\) /-]*)\n([\w /]*)\n([\w /]*)\n;;',
    #         text)

    # etext += re.findall(
    #         r'(\d+/\d+/\d{4}.\d+:\d\d)\n(\d{4}-\d{8})()()\n([\w /]*)\n;;',
    #         text)


    return etext




