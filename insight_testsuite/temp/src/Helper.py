
def process_line(line):
    data = line.split("|")
    try:
        d = {
            "cmte_id" : data[0],
            "zip_code": data[10],
            "transaction_date": data[13],
            "transaction_amount": data[14],
            "other_id": data[15]
            }
        return d
    except:
        print line + "is not a valid entry"
        return False

def median(sortedList):
    n = len(sortedList)
    if n < 1:
        return None
    if n % 2 == 1:
        return int(round(sortedList[n//2],0))
    else:
        return int(round(sum(sortedList[n//2-1:n//2+1])/2.0,0))


"""

#Turns out using regex is pretty slow...
pattern = re.compile("(?P<cmte_id>[a-zA-Z0-9]+)\|.*\|.*\|.*\|.*\|.*\|.*\|.*\|.*\|.*\|(?P<zip_code>.+)\|.*\|.*\|(?P<transaction_date>.*)\|(?P<TRANSACTION_AMT>.*)\|(?P<OTHER_ID>.*)\|.*\|.*\|.*\|.*\|.*")
def process_line(line):
    result = pattern.match(line)
    if result:
        return result.groupdict()
    else:
        return False
"""
