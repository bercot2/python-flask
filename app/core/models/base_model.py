from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

db = SQLAlchemy()
migrate = Migrate()


class BaseModel(db.Model):
    __abstract__ = True

    @classmethod
    def save(cls, instance, commit=True):
        db.session.add(instance)
        if commit:
            db.session.commit()
        return instance

    @classmethod
    def bulk_save(cls, instances: list, commit=True):
        db.session.bulk_save_objects(instances)
        if commit:
            db.session.commit()
        return instances

    def save(self, commit=True):
        db.session.add(self)
        if commit:
            db.session.commit()
        return self

    def delete(self, commit=True):
        db.session.delete(self)
        if commit:
            db.session.commit()
