from db import db

class StoreModel(db.Model):
	__tablename__ = 'stores'

	# associate db columun names
	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String(80))

	items = db.relationship('ItemModel', lazy='dynamic')

	def __init__(self, name):
		self.name = name

	def json(self):
		return {'name': self.name, 'items': [item.json() for item in self.items.all()]}

	@classmethod  # Keeping classmethod here because it returns an object
	def find_by_name(cls, name):
		return cls.query.filter_by(name=name).first()

	def save_to_db(self):  # This code will both insert or update in DB - SQL Alchemy handles the magic
		db.session.add(self)
		db.session.commit()

	def delete_from_db(self):
		db.session.delete(self)
		db.session.commit()
