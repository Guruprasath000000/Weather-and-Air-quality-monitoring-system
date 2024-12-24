import os

class Config:
    SECRET_KEY = 'Guru12prasath@s'
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:Guru12prasath%s@localhost/myproject.users'
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    GOOGLE_OAUTH_CLIENT_ID = '541441980761-tmhlqs9pt59a43vicec0lc9o7j09rtsl.apps.googleusercontent.com'
    GOOGLE_OAUTH_CLIENT_SECRET = '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'
    GOOGLE_OAUTH_REDIRECT_URI = 'http://127.0.0.1:5000/google/login'