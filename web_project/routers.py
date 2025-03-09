class DatabaseRouter:
    def db_for_read(self, model, **hints):
        if model._meta.db_table == 'account':
            return 'account-db'
        elif model._meta.db_table == 'property':
            return 'property-db'
        return 'default'
    
    def db_for_write(self, model, **hints):
        if model._meta.db_table == 'account':
            return 'account-db'
        elif model._meta.db_table == 'property':
            return 'property-db'
        return 'default'
    
    def allow_relation(self, obj1, obj2, **hints):
        db1 = self.db_for_read(obj1.__class__)
        db2 = self.db_for_read(obj2.__class__)
        return db1 == db2
    
    def allow_migrate(self, db, app_label, model_name=None, **hints):
        if db == 'account-db':
            return model_name == 'account'
        elif db == 'property-db':
            return model_name == 'property'
        return model_name == 'default'