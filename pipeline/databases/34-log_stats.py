#!/usr/bin/env python3
""" Provides some stats about Nginx logs stored in MongoDB """

from pymongo import MongoClient

if __name__ == "__main__":
    client = MongoClient("mongodb://localhost:27017/")
    db = client.logs
    nginx_collection = db.nginx

    # Total number of logs
    total_logs = nginx_collection.count_documents({})
    print(f"{total_logs} logs")

    # Count for each HTTP method
    methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]
    print("Methods:")
    for method in methods:
        count = nginx_collection.count_documents({"method": method})
        print(f"\tmethod {method}: {count}")

    # Count of status check (method GET with path /status)
    status_check_count = nginx_collection.count_documents(
        {"method": "GET", "path": "/status"}
    )
    print(f"{status_check_count} status check")
