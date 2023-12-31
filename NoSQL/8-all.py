#!/usr/bin/env python3

""" Prototype: def list_all(mongo_collection):
Return an empty list if no document in the collection
mongo_collection will be the pymongo collection object"""


from pymongo import MongoClient


def list_all(mongo_collection):
    """List all documents in a collection"""

    if mongo_collection is None:
        return []
    return mongo_collection.find()
