from pymongo import MongoClient
from pymongo.cursor import Cursor


client = MongoClient()
db = client.sample_pymongo
Users = db.users

print(Users.find().count())

print(Users.find({'favorit_number': 7}).count())


def _get_results_to_json(data):
    """Get documents from a MongoDB search result.
    Transforms MongoDB BSON documents into JSON serializable documents.
    This process converts the ObjectIds into hexadecimal strings.
    Parameters
    ----------
    data : `~pymongo.cursor.Cursor`
        A MongoDB search result.
    Returns
    -------
    |list| of |dict|
        A list of JSON serializable documents.
    """
    if isinstance(data, Cursor):
        data = list(data)

    if isinstance(data, list):
        for doc in data:
            doc['_id'] = str(doc['_id'])
    elif isinstance(data, dict):
        data['_id'] = str(data['_id'])

    return data


print(_get_results_to_json(Users.find({})))