import csv
import requests

filename = "br_xtransaction_details.csv"
API_ENDPOINT = "http://localhost:3000/api/Trade"
API_ENDPOINT_2 = "http://localhost:3000/api/SetUp"
API_ENDPOINT_3 = "http://localhost:3000/api/queries/getResults"

data={}
r = requests.post(url = API_ENDPOINT_2, data = data)

with open(filename) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    for row in csv_reader:
        if (line_count<=10):
            line_count+=1
            continue

        data = {
                    "$class": "org.xpay.Trade",
                    "PaymentTokenID": row[0].replace("'",""),
                    "MerchantID": row[1].replace("'",""),
                    "Currency": row[2].replace("'",""),
                    "Amount": row[3].replace("'",""),
                    "DataTransactionID": row[5].replace("'",""),
                    "AccountType": row[10].replace("'",""),
                    "commodity": "resource:org.xpay.Commodity#Default",
                    "newOwner": "resource:org.xpay.Trader#DB",
                } 
        
        r = requests.post(url = API_ENDPOINT, data = data)
        print(r)
        line_count+=1
        if(line_count>11):
            break


data={}
r = requests.get(url = API_ENDPOINT_3, params={'param1':'p0KXsIfOW5UUPbsn4bi3JAoG9w8='})
print(r.text)            