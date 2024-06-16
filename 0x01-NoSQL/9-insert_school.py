#!/usr/bin/env python3
"""List All Documents."""


def insert_school(mongo_collection, **kwargs):
    """Func inserts a new document in a collection based on kwargs.

    Args:
        kwargs (list): list of obj to add to the document

    Returns:
        collections: collections in data base
    """
    new_collection = mongo_collection.insert_one(kwargs)
    
    return new_collection.inserted_id
