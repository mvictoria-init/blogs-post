
# postgresql://{user}:{password}@{host:port}/{db_name}

class Config:
    DEBUG = True
    SECRET_KEY = 'dev'
    
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://postgres:lolita28@127.0.0.1:5432/blogposts_db'
    
    CKEDITOR_PKG_TYPE = 'full'