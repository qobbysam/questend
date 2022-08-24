
import datetime
import os
from shared.shared import client, username,password, res_to_list, save_db_postgres
import json

last_update = datetime.datetime.now()

file_ =  os.path.join(os.getcwd(), 'last.json')
def getlast():

    f = open(file_)

    filel = json.load(f)

    last = filel['last']
    return  last

def updatelast(last):
    f = open(file_, 'w')
    #filel = json.load(f)
    filel = {}
    filel['last'] = last
    with open(file_, 'w') as fp:
        json.dump(filel, fp)

def updatelasterror(error):
    print(error)
    


def get_update():

    print("getting update")

    
    #from_date = getlast().strftime("%Y-%m-%d")
    last = getlast()

    dt = datetime.datetime.strptime(last, "%Y-%m-%d %H:%M:%S.%f")

    from_date = dt.strftime("%Y-%m-%d")

    print(from_date, " from")
    
    res_ = client.service.UpdateRetrieveCollectionSiteDetails(username, password, from_date)

    #print(res_)
    to_save = res_to_list(res_)

    print("to list complete")

    try:

        save_db_postgres(to_save)

        now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")
    
        updatelast(now)
        print("update complete")
    except Exception as e:

        updatelasterror(e)







    


if __name__ == '__main__':
    get_update()