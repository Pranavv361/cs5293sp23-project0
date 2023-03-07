# cs5293sp23-project0
# Author - Pranav Vichare
# Project - Extracting Incidents from Norman Police Department pdf file on website

Assumptions:
1. Nature of Incidents field contains values which are of a kind shown below.
   This Sentence Is Called As Start Case.
   This Sentence is Called as Title Case.
   this Sentence Is Called As camelCase.
   This sentence is called as sentence case.
   this_sentence_is_called_as_snake_case.
   this-sentence-is-called-as-kebab-case
   

Bugs:   
1. If the field starts with a word ALL CAPS, then the word will be concatenated to th Address field.
   
