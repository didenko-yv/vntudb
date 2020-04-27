from core.fee import Fee
from core.country import Country
from core.partner import Partner
from core.program import Program
from core.require import Require
from core.student import Student
from core.university import University
from core.organization import Organization

country_row = {"name": "Ukraine",
               "universities": 140,
               "organizations": 156,
               "region": "Східна Європа"}

org_row = {"name": "IEAA",
           "year": 1989,
           "universities": 1340,
           "students": 40560,
           "head": "Kendrick Lamar"}

partner_row = {"name": "Google",
               "contact_name": "ASAP Rocky",
               "type_relation": "info",
               "type_action": "development"}

university_row = {"name": "VNTU",
                  "accreditation": 4,
                  "year": 1965,
                  "address": "Khmelnytske shosse 95",
                  "num_organizations": 8,
                  "country_id": 1}

country = Country.add_to_db(country_row)
organization = Organization.add_to_db(org_row)
partner_row = Partner.add_to_db(partner_row)
university_row = University.add_to_db(university_row)