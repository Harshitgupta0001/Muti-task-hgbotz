import re
import os
from os import environ

id_pattern = re.compile(r'^.\d+$')
AUTH_CHANNEL = [int(ch) if id_pattern.search(ch) else ch for ch in environ.get('AUTH_CHANNEL', '-1002166149059').split()] # give channel id with seperate space. Ex : ('-10073828 -102782829 -1007282828')

BOT_TOKEN = os.environ.get("BOT_TOKEN", "")
API_ID = int(os.environ.get("API_ID", ""))
API_HASH = os.environ.get("API_HASH", "")
PICS = os.environ.get("PICS", "").split()
ADMIN = [int(admin) if id_pattern.search(admin) else admin for admin in environ.get('ADMINS', '6359874284').split()]
DB_URL = os.environ.get("DB_URL", "mongodb+srv://Yash_607:Yash_607@cluster0.r3s9sbo.mongodb.net/?retryWrites=true&w=majority")
DB_NAME = os.environ.get("DB_NAME", "hgbotz")
RemoveBG_API = os.environ.get("RemoveBG_API", "t8hJ9cZvco3TcVqaCX7nxM31")
IBB_API = os.environ.get("IBB_API", "4e0191b236c31bd9a42f6806b48a7ebe")
FORCE_SUB = os.environ.get("FORCE_SUB", "")
PORT = os.environ.get('PORT', '8080')          
LOG_CHANNEL = int(environ.get('LOG_CHANNEL', '-1002346166150'))
LOG_TEXT = """<i><u>👁️‍🗨️USER DETAILS</u>

○ ID : <code>{id}</code>
○ DC : <code>{dc_id}</code>
○ First Name : <code>{first_name}<code>
○ UserName : @{username}

By = {bot}</i>"""
