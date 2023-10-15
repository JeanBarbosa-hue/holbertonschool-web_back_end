#!/usr/bin/env python3
"""log stats module"""
from pymongo import MongoClient

def nginx_logs_stats(database, collection_name):
    """provides some stats about Nginx logs stored in MongoDB"""
    try:
        client = MongoClient('mongodb://127.0.0.1:27017')
        collection = client[database][collection_name]

        # Total logs count
        count_logs = collection.count_documents({})
        print(f'{count_logs} logs')

        # Count and print each HTTP method
        methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]
        print('Methods:')
        for method in methods:
            count_method = collection.count_documents({'method': method})
            print(f'\tMethod {method}: {count_method}')

        # Count and print status checks
        check = collection.count_documents({"method": "GET", "path": "/status"})
        print(f'{check} status check')

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    database = "logs"  # Your MongoDB database name
    collection_name = "nginx"  # Your collection name
    nginx_logs_stats(database, collection_name)
