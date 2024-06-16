#!/usr/bin/env python3
"""List All Documents."""


def update_topics(mongo_collection, name, topics):
    """Func inserts a new document in a collection based on kwargs.

    Args:
        kwargs (list): list of obj to add to the document

    Returns:
        collections: collections in data base
    """
    return mongo_collection.update_many({"name": name}, {"$set": {"topics": topics}})
