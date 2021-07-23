from db import db


class Shark(db.Model):
    pk = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text, nullable=False)
    img_path = db.Column(db.String(100), nullable=True)
    video_id = db.Column(db.String(16), nullable=True)

    def __repr__(self):
        return self.name


class Oceanarium(db.Model):
    pk = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text, nullable=False)
    img_path = db.Column(db.String(100), nullable=True)
    iframe_src = db.Column(db.String(500), nullable=False)

    def __repr__(self):
        return self.name


class CageDivingPlace(db.Model):
    pk = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text, nullable=False)
    iframe_src = db.Column(db.String(500), nullable=False)

    def __repr__(self):
        return self.name
