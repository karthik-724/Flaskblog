import os 
class Config:
    SECRET_KEY =  '5791628bb0b13ce0c676dfde280ba245'#os.environ.get('SECRET_KEY')
    SQLALCHEMY_DATABASE_URI =  'sqlite:///site.db'#os.environ.get('SQLALCHEMY_DATABASE_URI')
    MAIL_SERVER = 'smtp.office365.com'
    MAIL_PORT= 587
    MAIL_USE_TLS= True
    MAIL_USERNAME =  'karthik24jul@outlook.com' #os.environ.get('EMAIL_USER')
    MAIL_PASSWORD =  'Karthik@266'#os.environ.get('EMAIL_PASS')
