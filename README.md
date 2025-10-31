# Marc_OA_Metadata
This script that adds Open Access 506 fields to MARC records for Open Access materials.

# dependencies
To use this script, install pymarc.

# Input
The expected input is .mrc files of electronic version record. The script checks for 506 values in the records in this .mrc file. If there is no 506, it will add it. If there is a 506 but the encoding level is 7 or M, it will remove the 506 and add a new one. If the encoding level is not 7 or 8, it will leave the 506 and add a new one.

# Output
The script creates an output file that is also .mrc, and writes the revised MARC records to it.
