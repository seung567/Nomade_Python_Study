from alba import alba_url_val, link_title, alba_info, alba_search
import csv
import os

url_list = alba_url_val()

for i in url_list:

    name, link = link_title(i)

    tr, count = alba_info(link, name)
    if count == "0":
        print("채용공고없음")
    else:
      
        flie = open(f"{name}.csv", mode="w")
        writer = csv.writer(flie)
        counters = len(tr)
        num = 0
        for i in tr:

            jobs_list_info = alba_search(i, name)

            writer.writerow(list(jobs_list_info['jobs'].values()))
            num += 1
            num_count = (num/counters)*100
            print(f"{num_count}% 완료")
