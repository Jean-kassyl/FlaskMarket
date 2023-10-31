from market import db, bcrypt


class Users(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    username = db.Column(db.String(length=30), nullable=False, unique=True)
    user_email = db.Column(db.String(length=60), nullable=False, unique=True)
    hash_pass = db.Column(db.String(), nullable=False)
    budget = db.Column(db.Integer(), nullable=False, default=1000)
    items = db.relationship('Item', backref="owner_user", lazy=True)

    @property
    def password(self):
        return self.password
    
    @password.setter
    def password(self, plain_password):
        self.hash_pass = bcrypt.generate_password_hash(plain_password).decode('utf-8')



class Item(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(length=30), nullable=False,unique=True )
    price = db.Column(db.Integer(), nullable=False)
    barcode = db.Column(db.String(length=12), nullable=False, unique=True)
    description = db.Column(db.String(), nullable=False)
    owner = db.Column(db.Integer(), db.ForeignKey('users.id'))

    def __repr__(self):
        return "Item N°{}, name: {} )".format(self.id, self.name)

