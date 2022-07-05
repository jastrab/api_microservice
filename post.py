"""
Modul pre prispevky so spracovanim API REST poziadaviek
"""

from flask import make_response, abort
from config import db
from models import Post, PostSchema
from external_api import getExternalApiPost, getExternalApiUser

def get_all():
    """
    Funkcia pre kompletny zoznam prispevkov

    :return:    zoznam vsetkych prispevkov v json formate
    """
    posts = Post.query.order_by(Post.id).all()
    post_schema = PostSchema(many=True)
    data = post_schema.dump(posts)
    return data


def get(id):
    """
    Funkcia pre nacitanie prispevku z databazy
    Pokial sa nenajde, tak sa vykona:
    - stiahnutie dat z externej api
    - zavolanie funkcie create a pridanie dat z externej api

    :param id:   Id prispevku
    :return:     200 ok, prispevok sa nasiel
                 404 chyba, prispevok sa nenasiel cez externu api
                 000 dalsie statusy podla funkcie create 
    """
    # Nacitanie prispevku z DB
    post = Post.query.filter(Post.id == id).one_or_none()

    # Ak s aprispevok nasiel v DB
    if post is not None:
        # Prevod z objekt DB na json format
        post_schema = PostSchema()
        data = post_schema.dump(post)
        return data, 200

    else:
        data = getExternalApiPost(id)
        # Ak vrati error, prispevok sa nepodarilo nacitat z externej api    
        if 'error' in data:
            abort(
                404,
                "Prispevok s id {id} sa nenasiel cez externu api".format(id=id),
            )
        # Ak sa prispevok nasiel, tak sa posle cez create do DB
        else:
            create(data)


def create(post_data):
    """
    Funkcia pre vytvorenie noveho prispevku na zaklade post_data

    :param json post_data:  data prispevoku pre vytvorenie  person to create in people structure
    :return:                201 ok, data pridane do DB
                            406 chyba, pouzivatel sa nenasiel
                            409 chyba, prispevok uz existuje
    """
    
    id     = post_data.get("id")
    userId = post_data.get("userId")
    
    post_exists = (
        Post.query.filter(Post.id == id)
        .one_or_none()
    )

    #Nacitanie id uzivatela, cez externe API
    user_exists = getExternalApiUser(userId)
    
    #Ak je error, tak vratilo prazdne data
    if 'error' in user_exists:
        abort(
            404,
            "Pouzivatel s id {id} neexistuje".format(id=userId),
        )
    # Prispevok nesmie existovat
    if post_exists is None:

        # Vytvori schemu pre prispevok a nacita data do modelu Post
        schema = PostSchema()
        post_new = schema.load(post_data, session=db.session)

        # Prida prispevok do DB
        db.session.add(post_new)
        db.session.commit()

        # Prevedie data z modelu do jsonu
        data = schema.dump(post_new)

        return data, 201

    # Prispevok uz existuje
    else:
        abort(
            409,
            "Prispevok s id {id} uz existuje".format(id=id),
        )


def update(id, post_data):
    """
    Funkcia pre aktualizáciu existujúceho príspevku

    Vráti chybu, pokiaľ aktualizované dáta sú zhodné s existujúcimi
    Vráti chybu, pokiaľ id prispevku nie je v DB

    Id pouzivatela sa tu neoveruje, kedze zmena je iba pri title, body
    
    :param int  id:          id prispevku, ktory cheme aktualizovat
    :param json post_data:   data na aktualizaciu prispevku
    :return:                 200 ok, vrati strukturu prispevku
                             404 chyba, prispevok sa nenasiel
                             409 chyba, uz existuje
    """
    # Vyziada prispevok z DB na zaklade id
    post_upd = Post.query.filter(
        Post.id == id
    ).one_or_none()

    # vyziada rovnaky prispevok z DB ako je aktualizovany aj so vsetkymi rovnakymi hodnotami
    id     = post_data.get("id")
    userId = post_data.get("userId")
    title  = post_data.get("title")
    body   = post_data.get("body")

    post_exists = (
        Post.query.filter(Post.id == id)
        .filter(Post.userId == userId)
        .filter(Post.title == title)
        .filter(Post.body == body)
        .one_or_none()
    )

    # pokial sa nenaslo id v DB, tak nemoze aktualizovat prispevok
    if post_upd is None:
        abort(
            404,
            "Prispevok s id {id} sa nenasiel!".format(id=id),
        )

    # aktualizovany prispevok uz existuje
    elif (
        post_exists is not None and post_exists.id != id
    ):
        abort(
            409,
            "Prispevok s id {id} uz existuje".format(id=id),
        )

    # ak je vsetko v poriadku, prejde sa na update
    else:
        # Fix pre aktualizaciu - kedze SQL Alchemy vyhadzuje chybu 
        # s chybajucimi datami, tj tie co su nullable
        # Preto zoberiem strukturu dat z DB
        # a doplnim mu upravene data
        post_upd.setDataFromJson(post_data)

        # schema prevedie Model na objekt DB
        schema = PostSchema()

        # spoji novy objekt zo starym
        db.session.merge(post_upd)

        # commitne/ulozi ju do DB
        db.session.commit()

        # prevedie data spat z objekt DB na Model
        data = schema.dump(post_upd)

        # vrati aktualizovany prispevok
        return data, 200


def delete(id):
    """
    Funkcia pre zmazanie prispevku z DB

    :param id:   id prispevku pre zmazanie
    :return:     200 ok, pre uspesne zmazanie
                 404 chyba, prispevok sa nenasiel
    """
    # Ziskanie prispevku z databazy
    post = Post.query.filter(Post.id == id).one_or_none()

    # Ak sa prispevku najde v DB
    if post is not None:
        db.session.delete(post)
        db.session.commit()
        return make_response(
            "Prispevok s id {id} uspesne zamazny!".format(id=id), 
            200
        )

    # Prispevok sa nenasiel v DB
    else:
        abort(
            404,
            "Prispevok s id {id} sa nenasiel v DB!".format(id=id),
        )


