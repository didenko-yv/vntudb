import os
import datetime

import sys
sys.path.append('..')

from flask_user import db_manager
from core.config import db, app


class Partner(db.Model):

    __tablename__ = 'partners'

    id = db.Column(db.Integer(), primary_key=True)
    company_name = db.Column(db.Unicode(100), nullable=False)
    contact_person = db.Column(db.Unicode(100), nullable=True)
    contact_phone = db.Column(db.Unicode(100), nullable=False)
    finances = db.Column(db.Integer(), nullable=False, default=0)
    activity = db.Column(db.Unicode(100), nullable=False)

    def get_data(self):
        row = {}
        for c in self.__table__.columns:
            row[c.name] = getattr(self, c.name)
        return row

    @staticmethod
    def get_by_id(_id):
        obj = Partner.query.filter_by(id=_id).first()
        return obj if obj is not None else False

    @staticmethod
    def update_by_id(raw):
        _id = raw['id']
        obj = Partner.get_by_id(_id)
        for r in raw:
            if hasattr(obj, r):
                setattr(obj, r, raw[r])
        db.session.commit()
        return obj.get_data()

    @staticmethod
    def delete_by_id(_id):
        obj = Partner.query.filter_by(id=_id).first()
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
        objs = Partner.query.all()
        return [o.to_dict() for o in objs] if objs else []

    @staticmethod
    def add_to_db(raw):
        obj = Partner()
        obj.company_name = raw['company_name']
        obj.contact_person = raw['contact_person']
        obj.contact_phone = raw['contact_phone']
        obj.finances = raw['finances']
        obj.activity = raw['activity']

        db.session.add(obj)
        db.session.commit()
        return obj.to_dict()

    @staticmethod
    def get_Partner(schedule=None, tax=None):
        obj = None

        if schedule and tax:
            obj = Partner.query.filter(Partner.schedule == schedule, Partner.tax == tax).all()
        elif schedule:
            obj = Partner.query.filter_by(schedule=schedule).all()
        elif tax:
            obj = Partner.query.filter_by(tax=tax).all()
        return obj if obj is not None else []


if __name__ == '__main__':
    db.create_all()
    db.session.commit()