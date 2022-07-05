"""
Modul pre pouzivatelov so spracovanim API REST poziadaviek
"""

from flask import make_response, abort
from config import db
from models import Post, PostSchema
from external_api import getExternalApiPost, getExternalApiUser

def get_posts(userId):
    """
    Funkcia pre ziskanie prispevkov na zaklade id pouzivatela

    :param userId:  id pouzivatela
    :return:        200 ok, zoznam prispevkov
                    404 chyba, pouzivatel alebo prispevky sa nenasli 
    """

    user_exists = getExternalApiUser(userId)
    if 'error' in user_exists:
        abort(
            404,
            "Pouzivatel s id {id} sa nenasiel".format(
                id=userId
            ),
        )
    else:

        # Vytvori zoznam prispevkov od daneho pouzivatela
        posts = Post.query.filter(Post.userId == userId).all()

        #Ak nevrati ziadny prispevok, vrati chybu
        if posts is None or len(posts) == 0:
            abort(
                404,
                "Ziadne prispevky pre pouzivatela s id: {id}".format(id=userId),
            )
        #Ak ok, vrati prislusne data
        else:
            post_schema = PostSchema(many=True)
            data = post_schema.dump(posts)
            return data, 200


def get(userId):
    """
    Funkcia pre ziskanie dat pouzivatela z externej API
    :param userId:  id pouzivatela
    :return:        200 ok, vrati data pre pouzivatela
                    404 chyba, pouzivatel sa nenasiel 
    """
    user_exists = getExternalApiUser(userId)
    if 'error' in user_exists:
        abort(
            404,
            "Pouzivatel s id {id} sa nenasiel".format(
                id=userId
            ),
        )
    else:
        return user_exists, 200
    