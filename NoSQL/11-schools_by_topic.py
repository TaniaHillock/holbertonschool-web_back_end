#!/usr/bin/env python3
""" Prototype: def schools_by_topic(mongo_collection, topic)"""

from pymongo import MongoClient


def schools_by_topic(mongo_collection, topic):
    """returns the list of schools having a specific topic"""
    if mongo_collection is None:
        return []

    return mongo_collection.find({'topics': topic})
