from db import db

class ItemModel(db.Model):
	__tablename__ = 'items'

	# associate db columun names
	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String(80))
	price = db.Column(db.Float(precision=2))  # this creates FLoating Point number with 2 decimal places precision

	store_id = db.Column(db.Integer, db.ForeignKey('stores.id'))
	store = db.relationship('StoreModel')

	def __init__(self, name, price, store_id):
		self.name = name
		self.price = price
		self.store_id = store_id

	def json(self):
		return {'name': self.name, 'price': self.price}

	@classmethod  # Keeping classmethod here because it returns an object
	def find_by_name(cls, name):
		return cls.query.filter_by(name=name).first()

	def save_to_db(self):  # This code will both insert or update in DB - SQL Alchemy handles the magic
		db.session.add(self)
		db.session.commit()

	def delete_from_db(self):
		db.session.delete(self)
		db.session.commit()
