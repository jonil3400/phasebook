from unicodedata import name
from flask import Blueprint, request

from .data.search_data import USERS

from itertools import groupby

bp = Blueprint("search", __name__, url_prefix="/search")


@bp.route("")
def search():
    return search_users(request.args.to_dict()), 200

def search_users(args):
    
    """Search users database

    Parameters:
        args: a dictionary containing the following search parameters:
            id: string
            name: string
            age: string
            occupation: string

    Returns:
        a list of users that match the search parameters
    """

    # Implement search here!

    userlist = []
    idvalue = None
    namevalue = None
    agevalue = None
    occvalue = None

    for key in args.keys():
        if key == "id":
            idvalue = args.get(key)
        elif key == "name":
            namevalue = args.get(key)
        elif key == "age":
            agevalue = args.get(key)
        elif key == "occupation":
            occvalue = args.get(key)
        
            

    for index in range(len(USERS)):
         #for ukey, uval in USERS[index].items():
        for key in USERS[index].keys():
            if idvalue != None and idvalue == USERS[index]['id']:
                userlist.append(index)    
            if namevalue != None and namevalue <= USERS[index]['name']:
                userlist.append(index)
            if agevalue != None and (int(agevalue) == int(USERS[index]['age']) or int(agevalue)+1 == int(USERS[index]['age']) or int(agevalue)-1 == int(USERS[index]['age'])):
                userlist.append(index)
            if occvalue != None and occvalue == USERS[index]['occupation']:
                userlist.append(index)
                    

    g = [k for k,_ in groupby(userlist)]

    return[USERS[i] for i in g]
