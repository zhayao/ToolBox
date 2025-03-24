import datetime

CURRENT_DATE = datetime.datetime.strptime("2024-12-31", "%Y-%m-%d")
TRAVEL_HIS ="""
5	2024-12-01	Arrival	KGW
6	2024-11-27	Departure	841
7	2024-11-03	Arrival	SEA
8	2024-10-19	Departure	SEA
9	2024-09-14	Arrival	BLA
10	2024-09-08	Departure	840
11	2024-09-07	Arrival	PHY
12	2024-09-06	Departure	SFR
13	2024-08-28	Arrival	VCV
14	2024-08-25	Departure	841
15	2024-08-22	Arrival	BLA
16	2024-08-16	Departure	840
17	2024-08-04	Arrival	KGW
18	2024-07-29	Departure	840
19	2024-07-27	Arrival	BLA
20	2024-07-13	Departure	840
21	2024-07-06	Arrival	KGW
22	2024-05-20	Departure	840
23	2024-05-12	Arrival	PHY
24	2024-05-03	Departure	840
25	2024-04-25	Arrival	BLA
26	2024-04-16	Departure	840
27	2024-04-12	Arrival	BLA
28	2024-03-24	Departure	840
29	2024-03-16	Arrival	BLA
30	2024-03-12	Departure	840
31	2024-03-12	Arrival	BLA
32	2024-03-08	Departure	813
33	2024-01-26	Arrival	BLA
34	2024-01-02	Departure	840
"""


TRAVEL_HIS = list(zip(TRAVEL_HIS.split()[1::4], TRAVEL_HIS.split()[2::4]))

def clean_up_records(hist):
    res = []
    for i in range(0, len(hist)):
        if len(res) > 0 and res[-1][0] == hist[i][0]:
            res.pop(-1)
        else:
            res.append(hist[i])
    return res

def get_tuples(hist, cur_date):
    res = []
    if hist[0][1] == "Departure":
        hist = [(cur_date.strftime("%Y-%m-%d"), "Arrival")] + hist
    for i in range(0, len(hist) // 2):
        res.append((hist[2*i][0], hist[2*i + 1][0]))
    if len(hist) % 2 == 0:
        return res
    else:
        res.append((hist[-1][0], cur_date.replace(month=1, day=1).strftime("%Y-%m-%d")))
        return res
    
def get_days(hist):
    n_days = 0
    for x, y in hist:
        n_days += (datetime.datetime.strptime(x, "%Y-%m-%d") - datetime.datetime.strptime(y, "%Y-%m-%d")).days + 1
    return n_days

cleanedRecord = clean_up_records(TRAVEL_HIS)
pairedRecord = get_tuples(cleanedRecord, CURRENT_DATE)

print("following is the days that you are outside of the States (implying you are in CA)")
print(pairedRecord)

print("based on the record, here's the total days you stayed in Canada if there is no any thrid country trips involved.")
print(get_days(pairedRecord))