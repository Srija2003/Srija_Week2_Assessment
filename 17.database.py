from abc import ABC, abstractmethod

class IDatabaseOperations(ABC):
    @abstractmethod
    def insert(self, data):
        pass
    
    @abstractmethod
    def update(self, data):
        pass
    
    @abstractmethod
    def delete(self, record_id):
        pass

class SQLDatabase(IDatabaseOperations):
    def insert(self, data):
        print(f"Inserting {data} into SQL database.")
    
    def update(self, data):
        print(f"Updating record in SQL database with {data}.")
    
    def delete(self, record_id):
        print(f"Deleting record {record_id} from SQL database.")

class NoSQLDatabase(IDatabaseOperations):
    def insert(self, data):
        print(f"Inserting {data} into NoSQL database.")
    
    def update(self, data):
        print(f"Updating document in NoSQL database with {data}.")
    
    def delete(self, record_id):
        print(f"Deleting document {record_id} from NoSQL database.")


sql_db = SQLDatabase()
sql_db.insert({"name": "Alice", "age": 25})
sql_db.update({"id": 1, "name": "Alice Cooper"})
sql_db.delete(1)

nosql_db = NoSQLDatabase()
nosql_db.insert({"username": "john_doe", "followers": 100})
nosql_db.update({"username": "john_doe", "followers": 150})
nosql_db.delete("abc123")
