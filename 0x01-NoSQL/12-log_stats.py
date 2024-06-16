#!/usr/bin/env python3
"""List All Documents."""

from pymongo import MongoClient

client = MongoClient('mongodb://127.0.0.1:27017')

nginx_collection = client.logs.nginx


numoflogs = nginx_collection.count_documents({})

numofGET = nginx_collection.count_documents({"method": "GET"})
numofPOST = nginx_collection.count_documents({"method": "POST"})
numofPUT = nginx_collection.count_documents({"method": "PUT"})
numofPATCH = nginx_collection.count_documents({"method": "PATCH"})
numofDELETE = nginx_collection.count_documents({"method": "DELETE"})
numofSTATUS = nginx_collection.count_documents({
    "path": "/status",
    "method": "GET"
    })

print(f"{numoflogs} logs",
      "\nMethods:",
      f"\n\tmethod GET: {numofGET}",
      f"\n\tmethod POST: {numofPOST}",
      f"\n\tmethod PUT: {numofPUT}",
      f"\n\tmethod PATCH: {numofPATCH}",
      f"\n\tmethod DELETE: {numofDELETE}"
      f"\n{numofSTATUS} status check")
