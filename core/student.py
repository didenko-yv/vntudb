import os
import datetime

import sys
sys.path.append('..')

from flask_user import db_manager
from core.config import db, app


class Student(db.Model):

    __tablename__ = 'students'

    id = db.Column(db.Integer(), primary_key=True)
    full_name = db.Column(db.Unicode(100), nullable=False)
    phone_number = db.Column(db.Unicode(100), nullable=True)
    program = db.Column(db.Unicode(100), nullable=False)
    college = db.Column(db.Unicode(100), nullable=False, default=0)
    specialization = db.Column(db.Unicode(100),nullable=False)
    year_study = db.Column(db.Integer(), nullable=False)
    foreign_language = db.Column(db.Unicode(100), nullable=False)
    progress = db.Column(db.Unicode(100), nullable=False)

    def get_data(self):
        row = {}
        for c in self.__table__.columns:
            row[c.name] = getattr(self, c.name)
        return row

    @staticmethod
    def get_by_id(_id):
        obj = Student.query.filter_by(id=_id).first()
        return obj if obj is not None else False

    @staticmethod
    def update_by_id(raw):
        _id = raw['id']
        obj = Student.get_by_id(_id)
        for r in raw:
            if hasattr(obj, r):
                setattr(obj, r, raw[r])
        db.session.commit()
        return obj.get_data()

    @staticmethod
    def delete_by_id(_id):
        obj = Student.query.filter_by(id=_id).first()
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
        objs = Student.query.all()
        return [o.to_dict() for o in objs] if objs else False

    @staticmethod
    def add_to_db(raw):
        obj = Student()
        obj.full_name = raw['full_name']
        obj.phone_number = raw['phone_number']
        obj.program = raw['program']
        obj.specialization = raw['specialization']
        obj.college = raw['college']
        obj.year_study = raw['year_study']
        obj.foreign_language = raw['foreign_language']
        obj.progress = raw['progress']

        db.session.add(obj)
        db.session.commit()
        return obj.to_dict()

    @staticmethod
    def get_vacancy(schedule=None, tax=None):
        obj = None

        if schedule and tax:
            obj = Student.query.filter(Student.schedule == schedule, Student.tax == tax).all()
        elif schedule:
            obj = Student.query.filter_by(schedule=schedule).all()
        elif tax:
            obj = Student.query.filter_by(tax=tax).all()
        return obj if obj is not None else False


if __name__ == '__main__':
    db.create_all()
    db.session.commit()