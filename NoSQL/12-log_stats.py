#!/usr/bin/env python3
""" Log stats """
from pymongo import MongoClient

def print_logs_stats(collection):
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

if __name__ == "__main__":
    try:
        client = MongoClient('mongodb://127.0.0.1:27017')
        db_nginx = client.logs.nginx
        print_logs_stats(db_nginx)
    except Exception as e:
        print(f"An error occurred: {e}")

