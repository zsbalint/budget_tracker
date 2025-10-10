import os

# base directory of the project (one level above flaskr)
BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))

# instance and uploads folders
INSTANCE_DIR = os.path.join(BASE_DIR, "instance")
UPLOAD_FOLDER = os.path.join(BASE_DIR, "uploads")

class Config:
    SECRET_KEY = os.environ.get("SECRET_KEY", "dev_secret")
    ALLOWED_EXTENSIONS = {'csv', 'xls', 'xlsx', 'ods'}
    MAX_CONTENT_LENGTH = 16 * 1024 * 1024  # 16 MB

    # paths
    UPLOAD_FOLDER = UPLOAD_FOLDER
    DATABASE = os.path.join(INSTANCE_DIR, "flaskr.sqlite")
