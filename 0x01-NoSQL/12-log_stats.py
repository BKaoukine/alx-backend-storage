#!/usr/bin/env python3
"""
List All Documents.

This script connects to a MongoDB database, counts the number of logs
and specific HTTP method occurrences, and prints the results.
"""

from pymongo import MongoClient


def count_documents(collection, query):
    """Count documents in the collection based on a query.

    Args:
        collection: The MongoDB collection object.
        query: The query to filter documents.

    Returns:
        The count of documents matching the query.
    """
    return collection.count_documents(query)


def main():
    """Main function to connect to MongoDB and count log entries."""
    # Connect to the MongoDB server
    client = MongoClient('mongodb://127.0.0.1:27017')
    nginx_collection = client.logs.nginx

    # Count total number of logs
    num_of_logs = count_documents(nginx_collection, {})

    # Count number of logs for each HTTP method
    num_of_get = count_documents(nginx_collection, {"method": "GET"})
    num_of_post = count_documents(nginx_collection, {"method": "POST"})
    num_of_put = count_documents(nginx_collection, {"method": "PUT"})
    num_of_patch = count_documents(nginx_collection, {"method": "PATCH"})
    num_of_delete = count_documents(nginx_collection, {"method": "DELETE"})

    # Count number of status check logs
    num_of_status = count_documents(nginx_collection, {
        "path": "/status",
        "method": "GET"
    })

    # Print the results
    print(f"{num_of_logs} logs")
    print("Methods:")
    print(f"\tmethod GET: {num_of_get}")
    print(f"\tmethod POST: {num_of_post}")
    print(f"\tmethod PUT: {num_of_put}")
    print(f"\tmethod PATCH: {num_of_patch}")
    print(f"\tmethod DELETE: {num_of_delete}")
    print(f"{num_of_status} status check")


if __name__ == "__main__":
    main()
