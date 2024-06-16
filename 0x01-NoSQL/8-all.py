#!/usr/bin/env python3
"""List All Documents."""


def list_all(mongo_collection):
    """List All function gets all documents in a given collection.

    Args:
        mongo_collection (monpy object): collection object

    Returns:
        collections: collections in data base
    """
    if mongo_collection is None:
        return []

    return mongo_collection.find()
