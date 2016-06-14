from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext.migrate import Migrate, MigrateCommand
from app import app


app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://username:password@hostname/database'
app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True
db = SQLAlchemy(app)
migrate = Migrate(app, db)


class Role(db.Model):
    __tablename__ = 'roles'
    id = db.Column(db.Sequence, primary_key=True)
    name = db.Column(db.String(64))

    def __repr__(self):
        return '<Role %r>' % self.name


# usertype 类型需要外键关联到 roles 表
class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Sequence, primary_key=True)
    username = db.Column(db.String(64), index=True)
    usertype = db.Column()
    birthday = db.Column(db.DATE)
    address = db.Column(db.String(256))
    email = db.Column(db.String(64))
    phone = db.Column(db.CHAR(16))

    def __repr__(self):
        return '<User %r>' % self.username


class Article(db.Model):
    __tablename__ = 'articles'
    id = db.Column(db.Sequence, primary_key=True)
    title = db.Column(db.String(256), index=True)
    content = db.Column(db.TEXT)

