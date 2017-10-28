import sys
import os
import Entity
from Helper import process_line

dir_path = os.path.dirname(os.path.realpath(__file__))
path = sys.argv[1];

f = open(path, "r") #input file object
byzip = open(dir_path + "/../output/medianvals_by_zip.txt", "w+")

zip_dict = {} #key: zip code, value: ()
for line in f:
    d = process_line(line)
    print d
    entity = Entity(d["cmte_id"], d[zip_code], d["transction_date"], d["transction_amount"], d["other_id"])




bydate = open(dir_path + "/../output/medianvals_by_date.txt", "w+")


f.close()
