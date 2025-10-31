#!/usr/bin/env python
# coding: utf-8

pip install pymarc

#import attributes
from pymarc import Record, Field, Subfield, Indicators, MARCReader

#importing an attribute to make a new copy
from copy import deepcopy

#define input file
input_file = 'filename.mrc'

#create new 506 string
new_506 = Field(
        tag = '506',
        indicators = Indicators('0',' '),
        subfields = [
            Subfield(code='3', value='Some versions: '),
            Subfield(code='a', value='Open access versions available from some providers '),
            Subfield(code='f', value='Unrestricted online access '),
            Subfield(code='2', value='star')
        ])

#open input file
my_edited_record = []
with open(input_file, 'rb') as data:
    reader = MARCReader(data)
    for record in reader:
        my_record = deepcopy(record)
  
#get the 506s
        my_506s = my_record.get_fields('506')

#get the leader
        leader = my_record.leader

#add a 506 if there is none
        if len(my_506s) == 0:
            my_record.add_ordered_field(new_506)
#if there is a 506 that includes Open Access, check if the encoding level is 7 or M, and remove if it is
        else:
            for my_506 in my_506s:
                if 'Open access' in my_506.value():
                    if '7' in leader[17]:
                        my_record.remove_field(my_506); my_record.add_ordered_field(new_506)
                    elif 'M' in leader[17]:
                        my_record.remove_field(my_506); my_record.add_ordered_field(new_506)
                    else:
                        my_record.add_ordered_field(new_506)
                else:
                    my_record.add_ordered_field(new_506)

#add new record to list of edited records
        my_edited_record.append(my_record)
        
#create output file and write to it
output_file = 'outputfilename.mrc'
with open(output_file , 'wb') as data: 
    for my_record in my_edited_record:
        data.write(my_record.as_marc())


