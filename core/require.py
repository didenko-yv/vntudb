import os
import datetime

import sys
sys.path.append('..')

from flask_user import db_manager
from core.config import db, app


class Require(db.Model):

    __tablename__ = 'requires'

    id = db.Column(db.Integer(), primary_key=True)
    college = db.Column(db.Unicode(100), nullable=False)
    program_type = db.Column(db.Unicode(100), nullable=True)
    progress = db.Column(db.Unicode(100), nullable=False)
    language = db.Column(db.Unicode(100), nullable=False)
    economy_region = db.Column(db.Unicode(100), nullable=False)
    year_study = db.Column(db.Integer(), nullable=False)

    def get_data(self):
        row = {}
        for c in self.__table__.columns:
            row[c.name] = getattr(self, c.name)
        return row

    @staticmethod
    def get_by_id(_id):
        obj = Require.query.filter_by(id=_id).first()
        return obj if obj is not None else []

    @staticmethod
    def update_by_id(raw):
        _id = raw['id']
        obj = Require.get_by_id(_id)
        for r in raw:
            if hasattr(obj, r):
                setattr(obj, r, raw[r])
        db.session.commit()
        return obj.get_data()

    @staticmethod
    def delete_by_id(_id):
        obj = Require.query.filter_by(id=_id).first()
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
        objs = Require.query.all()
        return [o.to_dict() for o in objs] if objs else []

    @staticmethod
    def add_to_db(raw):
        obj = Require()
        obj.college = raw['college']
        obj.program_type = raw['program_type']
        obj.progress = raw['progress']
        obj.language = raw['language']
        obj.economy_region = raw['economy_region']
        obj.year_study = raw['year_study']

        db.session.add(obj)
        db.session.commit()
        return obj.to_dict()

    @staticmethod
    def get_Require(schedule=None, tax=None):
        obj = None

        if schedule and tax:
            obj = Require.query.filter(Require.schedule == schedule, Require.tax == tax).all()
        elif schedule:
            obj = Require.query.filter_by(schedule=schedule).all()
        elif tax:
            obj = Require.query.filter_by(tax=tax).all()
        return obj if obj is not None else []


if __name__ == '__main__':
    db.create_all()
    db.session.commit()