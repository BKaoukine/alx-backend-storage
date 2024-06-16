#!/usr/bin/env python3
"""List All Documents."""


def schools_by_topic(mongo_collection, topic):
    """Func inserts a new document in a collection based on kwargs.

    Args:
        kwargs (list): list of obj to add to the document

    Returns:
        collections: collections in data base
    """
    return mongo_collection.find({"topics": {"$in": [topic]}})
