import os
import datetime

import sys
sys.path.append('..')

from flask_user import db_manager
from core.config import db, app


class Program(db.Model):

    __tablename__ = 'programs'

    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.Unicode(100), nullable=False)
    num_students = db.Column(db.Integer(), nullable=True)
    organization = db.Column(db.Unicode(100), nullable=False)
    college = db.Column(db.Unicode(100), nullable=False, default=0)
    sponsor = db.Column(db.Unicode(100), nullable=False)
    chief = db.Column(db.Unicode(100), nullable=False)
    field = db.Column(db.Unicode(100), nullable=False)

    def get_data(self):
        row = {}
        for c in self.__table__.columns:
            row[c.name] = getattr(self, c.name)
        return row

    @staticmethod
    def get_by_id(_id):
        obj = Program.query.filter_by(id=_id).first()
        return obj if obj is not None else []

    @staticmethod
    def update_by_id(raw):
        _id = raw['id']
        obj = Program.get_by_id(_id)
        for r in raw:
            if hasattr(obj, r):
                setattr(obj, r, raw[r])
        db.session.commit()
        return obj.get_data()

    @staticmethod
    def delete_by_id(_id):
        obj = Program.query.filter_by(id=_id).first()
        db.session.delete(obj)
        db.session.commit()
        return _id

    def to_dict(self):
        row = {}
        # exclude = ['schedule', 'tax']
        for c in self.__table__.columns:
            # if c.name not in exclude:
            row[c.name] = getattr(self, c.name)
        return row

    @staticmethod
    def to_dict_list(objs):
        return [o.to_dict() for o in objs]

    @staticmethod
    def get_all():
        objs = Program.query.all()
        return [o.to_dict() for o in objs] if objs else []

    @staticmethod
    def add_to_db(raw):
        obj = Program()
        obj.name = raw['name']
        obj.num_students = raw['num_students']
        obj.organization = raw['organization']
        obj.college = raw['college']
        obj.sponsor = raw['sponsor']
        obj.chief = raw['chief']
        obj.field = raw['field']

        db.session.add(obj)
        db.session.commit()
        return obj.to_dict()

    @staticmethod
    def get_vacancy(schedule=None, tax=None):
        obj = None

        if schedule and tax:
            obj = Program.query.filter(Program.schedule == schedule, Program.tax == tax).all()
        elif schedule:
            obj = Program.query.filter_by(schedule=schedule).all()
        elif tax:
            obj = Program.query.filter_by(tax=tax).all()
        return obj if obj is not None else []


if __name__ == '__main__':
    db.create_all()
    db.session.commit()