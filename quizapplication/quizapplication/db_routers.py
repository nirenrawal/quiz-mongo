# router.py

class DatabaseRouter:
    def db_for_read(self, model, **hints):
        if model._meta.app_label == 'quiz':
            return 'quiz'
        elif model._meta.app_label == 'user_registration':
            return 'default'
        return None

    def db_for_write(self, model, **hints):
        if model._meta.app_label == 'quiz':
            return 'quiz'
        elif model._meta.app_label == 'user_registration':
            return 'default'
        return None

    def allow_relation(self, obj1, obj2, **hints):
        return None
    # def allow_relation(self, obj1, obj2, **hints):
    #     if (obj1._meta.app_label == 'quiz' and obj2._meta.app_label == 'user_registration') or (obj1._meta.app_label == 'user_registration' and obj2._meta.app_label == 'quiz'):
    #         return True
    #     return False



    def allow_migrate(self, db, app_label, model_name=None, **hints):
        if app_label == 'quiz':
            return db == 'quiz'
        elif app_label == 'user_registration':
            return db == 'default'
        return None
