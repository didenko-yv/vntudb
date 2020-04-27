import os
import datetime

import sys
sys.path.append('..')

from flask_user import db_manager
from core.config import db, app


class College(db.Model):

    __tablename__ = 'colleges'

    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.Unicode(100), nullable=False)
    accreditation = db.Column(db.Integer(), nullable=True)
    address = db.Column(db.Unicode(100), nullable=False)
    year = db.Column(db.Integer(), nullable=False, default=0)
    country = db.Column(db.Unicode(100))

    def get_data(self):
        row = {}
        for c in self.__table__.columns:
            row[c.name] = getattr(self, c.name)
        return row

    @staticmethod
    def get_by_id(_id):
        obj = College.query.filter_by(id=_id).first()
        return obj if obj is not None else []

    @staticmethod
    def update_by_id(raw):
        _id = raw['id']
        obj = College.get_by_id(_id)
        for r in raw:
            if hasattr(obj, r):
                setattr(obj, r, raw[r])
        db.session.commit()
        return obj.get_data()

    @staticmethod
    def delete_by_id(_id):
        obj = College.query.filter_by(id=_id).first()
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
        objs = College.query.all()
        return [o.to_dict() for o in objs] if objs else []

    @staticmethod
    def add_to_db(raw):
        obj = College()
        obj.name = raw['name']
        obj.accreditation = raw['accreditation']
        obj.address = raw['address']
        obj.year = raw['year']
        obj.country = raw['country']

        db.session.add(obj)
        db.session.commit()
        return obj.to_dict()

    @staticmethod
    def get_College(schedule=None, tax=None):
        obj = None

        if schedule and tax:
            obj = College.query.filter(College.schedule == schedule, College.tax == tax).all()
        elif schedule:
            obj = College.query.filter_by(schedule=schedule).all()
        elif tax:
            obj = College.query.filter_by(tax=tax).all()
        return obj if obj is not None else []


if __name__ == '__main__':
    db.create_all()
    db.session.commit()