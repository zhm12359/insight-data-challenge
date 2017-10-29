import sys
import os
import bisect
from datetime import datetime
from Entity import Entity
from Helper import process_line, median

path = sys.argv[1]
outPath1 = sys.argv[2]
outPath2 = sys.argv[3]

f = open(path, "r") #input file object
byzip = open(outPath1, "w+")

zip_dict = {} #key: zip code, value: ordered list of transaction amount
id_dict = {} #key: cmte_id, value: list of Entities
for line in f:
    d = process_line(line)
    entity = Entity(d["cmte_id"], d["zip_code"], d["transaction_date"], d["transaction_amount"], d["other_id"])
    if entity.validate_zip_code():
        if entity.zip_code in zip_dict:
            bisect.insort(zip_dict[entity.zip_code], entity.transaction_amount) #log n insert and maintain order
        else:
            zip_dict[entity.zip_code] = [entity.transaction_amount]
        amounts = zip_dict[entity.zip_code]
        output = entity.cmte_id + "|" + entity.zip_code + "|" + str(median(amounts)) + "|" + str(len(amounts)) + "|" + str(sum(amounts)) + "\n"
        byzip.write(output)

    if entity.validate_date():
        if entity.cmte_id in id_dict:
            id_dict[entity.cmte_id].append(entity)
        else:
            id_dict[entity.cmte_id] = [entity]

f.close()
byzip.close()

bydate = open(outPath2, "w+")
ids = id_dict.keys()
ids.sort() # first sort by cmte_id

for cmte_id in ids:
    entities = id_dict[cmte_id]
    entities.sort(key=lambda x: x.transaction_date)
    date_map = {} #key: date, value: ordered list of transaction amount
    for e in entities:
        if e.transaction_date in date_map:
            bisect.insort(date_map[e.transaction_date], e.transaction_amount)
        else:
            date_map[e.transaction_date] = [e.transaction_amount]
        amounts = date_map[e.transaction_date]
    output = cmte_id + "|" + e.transaction_date.strftime("%m%d%Y")[0:8] + "|" + str(median(amounts)) + "|" + str(len(amounts)) + "|" + str(sum(amounts)) + "\n"
    bydate.write(output)

bydate.close()
