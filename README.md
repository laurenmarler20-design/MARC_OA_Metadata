# Marc_OA_Metadata
This script that adds open access 506 fields to MARC records for open access materials. It was created for an internship with Resource Acquisitions and Metadata Services at UCLA in fall 2025. 

# Dependencies
To use this script, install pymarc.

# Input
The expected input is a .mrc file that contains MARC records for open access titles. The script checks for 506 values in the records in this .mrc file. If there is no 506, it will add a specific 506 field: "ǂ3 Some versions: ǂa Open access versions available from some providers ǂf Unrestricted online access ǂ2 star". If there is a 506 but the encoding level is 7 or M, it will remove the existing 506 and add a new one. If the encoding level is not 7 or 8, it will leave the existing 506 and add a new one.

# Output
The script creates an output file that is also a .mrc, and writes the revised MARC records to it.

# License
This script is available under CC-BY-4.0
