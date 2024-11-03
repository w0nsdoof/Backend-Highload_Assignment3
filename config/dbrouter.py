from random import choice
from django.db.utils import OperationalError
from django.db import connections

class CustomDatabasesRouter:
    def db_for_read(self, model, **hints):

        db_list = ["replica", "default"]

        db_choice = choice(db_list)
        
        try:
            db_conn = connections[db_choice]
            db_conn.cursor()
        except OperationalError:
            print(f"{db_choice} is down !")            
            
            db_list.remove(db_choice)
            db_choice = db_list[0]
            
            print(f"Switching to {db_choice} for READ Query")
            
        print(f"performing READ query on {db_choice}")
        return db_choice

    def db_for_write(self, model, **hints):
        print(f"WRITE OPERATION using default")

        return "default"
    
    def allow_relation(self, obj1, obj2, **hints):
        return True

    def allow_migrate(self, db, app_label, model_name=None, **hints):
        return db == 'default'
    

