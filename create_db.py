"""
Vytvorenie DB, pripadne nacitanie testovacich udajov z externej api do DB
"""

import os

from config import db
from models import Post
from external_api import getExternalApiPostForDB

# Premazanie DB
# Problem s pravami priamo pod windows...
if os.path.exists('data.db'):
     os.remove('data.db')

# Vytvorenie DB
db.create_all()

# Nacitanie dat z externej API
def addToDB():
    for data in getExternalApiPostForDB(10):
        p = Post()
        p.setDataFromJson(data)
        # print ('wtf')
        print ('id=', p.id)
        print ('userId=', p.userId)
        print ('title=', p.title)
        print ('body=', p.body)
        db.session.add(p)

    db.session.commit()

addToDB()