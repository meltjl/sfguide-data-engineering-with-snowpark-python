
import shutil, os
import urllib.request 

# url of sample config
url = 'https://github.com/Snowflake-Labs/sfguide-data-engineering-with-snowpark-python/blob/main/.devcontainer/config'

# set path under current user profile
filepath = os.path.join(os.path.expanduser("~"), '.snowsql')

# target filename & filepath = .\snowsql\config must match C:\Users\User\Documents\tmp_repo\03-sfguide-data-engineering-with-snowpark-python\utils\snowpark_utils.py
filename = os.path.join(filepath, 'config')



# create file path 
if not os.path.exists(filepath):
    try:  
        os.mkdir(filepath)  
    except OSError as error:  
        print(error)  



# option1: download file in
urllib.request.urlretrieve(url, filename)


# option2: overwrite it 
text_file = open(filename, "w")
content = '''
# SnowSQL config

[connections.dev]
accountname = eg82070.ap-southeast-1
username = meltjl2024
password = iqg5VJ4uuN4wlaQKGXmq
rolename = HOL_ROLE
warehousename = HOL_WH
dbname = HOL_DB
schemaname = EXTERNAL

'''
text_file.write(content)
text_file.close()
