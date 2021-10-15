from db_connect import db

# 위생가게에 대한 데이터베이스
class cleanTable(db.Model):
    
    __tablename__ = 'clean_store'

    index = db.Column(db.Integer, primary_key=True, nullable=False)
    asgn_to = db.Column(db.Integer)
    prsdnt_nm = db.Column(db.String(255))
    hg_asgn_lv = db.Column(db.String(255))
    hg_asgn_ymd = db.Column(db.Integer)
    bssh_nm = db.Column(db.String(255))
    telno = db.Column(db.String(255))
    asgn_from = db.Column(db.Integer)
    lcns_no = db.Column(db.String(255))
    wrkr_reg_no = db.Column(db.Integer)
    induty_nm = db.Column(db.String(255))
    addr = db.Column(db.String(255))
    hg_asgn_no = db.Column(db.String(255))
    hg_asgn_nm = db.Column(db.String(255))
    franchise = db.Column(db.Integer)
    addr1 = db.Column(db.String(255))
    addr2 = db.Column(db.String(255))
