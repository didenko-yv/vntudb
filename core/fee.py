import os
import datetime

import sys
sys.path.append('..')

from flask_user import db_manager
from core.config import db, app


class Fee(db.Model):

    __tablename__ = 'fees'

    id = db.Column(db.Integer(), primary_key=True)
    program = db.Column(db.Unicode(100), nullable=False)
    sponsor = db.Column(db.Unicode(100), nullable=True)
    course_price = db.Column(db.Integer(), nullable=False)
    grant = db.Column(db.Integer(), nullable=False, default=0)
    living_cost = db.Column(db.Integer(), nullable=False, default=0)
    additional_cost = db.Column(db.Integer(), nullable=False, default=0)

    def get_data(self):
        row = {}
        for c in self.__table__.columns:
            row[c.name] = getattr(self, c.name)
        return row

    @staticmethod
    def get_by_id(_id):
        obj = Fee.query.filter_by(id=_id).first()
        return obj if obj is not None else False

    @staticmethod
    def update_by_id(raw):
        _id = raw['id']
        obj = Fee.get_by_id(_id)
        for r in raw:
            if hasattr(obj, r):
                setattr(obj, r, raw[r])
        db.session.commit()
        return obj.get_data()

    @staticmethod
    def delete_by_id(_id):
        obj = Fee.query.filter_by(id=_id).first()
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
        objs = Fee.query.all()
        return [o.to_dict() for o in objs] if objs else False

    @staticmethod
    def add_to_db(raw):
        obj = Fee()
        obj.program = raw['program']
        obj.sponsor = raw['sponsor']
        obj.course_price = raw['course_price']
        obj.grant = raw['grant']
        obj.living_cost = raw['living_cost']
        obj.additional_cost = raw['additional_cost']

        db.session.add(obj)
        db.session.commit()
        return obj.to_dict()

    @staticmethod
    def get_vacancy(schedule=None, tax=None):
        obj = None

        if schedule and tax:
            obj = Fee.query.filter(Fee.schedule == schedule, Fee.tax == tax).all()
        elif schedule:
            obj = Fee.query.filter_by(schedule=schedule).all()
        elif tax:
            obj = Fee.query.filter_by(tax=tax).all()
        return obj if obj is not None else False


if __name__ == '__main__':
    db.create_all()
    db.session.commit()