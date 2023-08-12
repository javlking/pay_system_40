from fastapi import FastAPI


app = FastAPI(docs_url='/')



# импорт всех компонентов
from api.convert import convert_api
from api.profile import profile_api
from api.transfers import transfers_api

"""
git init
git add .
git commit -m "message"
## From github ##
git remote add origin https://github.com/javlking/pay_system_40.git
git branch -M main
git push -u origin main


## Updates ##
git add .
git commit -m "message"
git push origin main
"""