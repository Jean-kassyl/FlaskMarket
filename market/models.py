from market import db, bcrypt, login_manager
from flask_login import UserMixin


@login_manager.user_loader
def load_user(users_id):
    return Users.query.get(int(users_id))

class Users(db.Model, UserMixin):
    id = db.Column(db.Integer(), primary_key=True)
    username = db.Column(db.String(length=30), nullable=False, unique=True)
    user_email = db.Column(db.String(length=60), nullable=False, unique=True)
    hash_pass = db.Column(db.String(), nullable=False)
    budget = db.Column(db.Integer(), nullable=False, default=1000)
    items = db.relationship('Item', backref="owner_user", lazy=True)


    @property
    def prettier_budget(self):
        if len(str(self.budget)) > 4:
            return f'{str(self.budget)[:-3]},{str(self.budget)[-3:]}$'
        else:
            return f"{self.budget}$"
    @property
    def password(self):
        return self.password
    
    @password.setter
    def password(self, plain_password):
        self.hash_pass = bcrypt.generate_password_hash(plain_password).decode('utf-8')


    def check_password(self, candidate):
        return bcrypt.check_password_hash(self.hash_pass, candidate)
    
    def __repr__(self):
        return f'{self.username} of id {self.id}'



class Item(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(length=30), nullable=False,unique=True )
    price = db.Column(db.Integer(), nullable=False)
    barcode = db.Column(db.String(length=12), nullable=False, unique=True)
    description = db.Column(db.String(), nullable=False)
    owner = db.Column(db.Integer(), db.ForeignKey('users.id'))

    def __repr__(self):
        return "Item N°{}, name: {} )".format(self.id, self.name)

