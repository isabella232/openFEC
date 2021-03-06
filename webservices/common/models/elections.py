from .base import db

from webservices import docs


class ElectionResult(db.Model):
    __tablename__ = 'ofec_election_result_mv'

    election_yr = db.Column(db.Integer, primary_key=True, doc=docs.ELECTION_YEAR)
    cand_office = db.Column(db.String, primary_key=True, doc=docs.OFFICE)
    cand_office_st = db.Column(db.String, primary_key=True, doc=docs.STATE_GENERIC)
    cand_office_district = db.Column(db.String, primary_key=True, doc=docs.DISTRICT)
    election_type = db.Column(db.String)
    fec_election_yr = db.Column(db.Integer)
    cand_id = db.Column(db.String, doc=docs.CANDIDATE_ID)
    cand_name = db.Column(db.String, doc=docs.CANDIDATE_NAME)


class ElectionsList(db.Model):
    __tablename__ = 'ofec_elections_list_mv'

    idx = db.Column(db.Integer, primary_key=True)
    sort_order = db.Column(db.Integer)
    office = db.Column(db.String, doc=docs.OFFICE)
    state = db.Column(db.String, doc=docs.STATE_GENERIC)
    district = db.Column(db.String, doc=docs.DISTRICT)
    cycle = db.Column(db.Integer)
    incumbent_id = db.Column(db.String, doc=docs.CANDIDATE_ID)
    incumbent_name = db.Column(db.String, doc=docs.CANDIDATE_NAME)


class ZipsDistricts(db.Model):
    __table_args__ = {'schema': 'staging'}
    __tablename__ = 'ref_zip_to_district'

    zip_district_id = db.Column(db.Integer, primary_key=True)
    district = db.Column(db.String, doc=docs.DISTRICT)
    zip_code = db.Column(db.String)
    state_abbrevation = db.Column(db.String)
    active = db.Column(db.String)
