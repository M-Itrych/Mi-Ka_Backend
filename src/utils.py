import datetime
import locale
import validators

from pymongo import MongoClient

def connect_to_mongodb():
    client = MongoClient('localhost', 27017)
    db = client.data
    return client, db

def close_mongodb_connection(client):
    client.close()

def serialize_id(data):
    if isinstance(data, list):
        for d in data:
            d['_id'] = str(d['_id'])
    elif isinstance(data, dict):
        data['_id'] = str(data['_id'])
    return data

def get_date_string():
    locale.setlocale(locale.LC_TIME, 'pl_PL.UTF-8')
    now = datetime.datetime.now()
    return now.strftime("%d %B %Y")


def validate_news(data):
    required_fields = {
        'title': "Tytuł nie został podany.",
        'desc': "Opis nie został podany.",
        'img': "Brakujące dane obrazu.",
        'text': "Brakująca treść artykułu."
    }

    if 'img' in data:
        img_data = data['img']
        if not all(key in img_data for key in ['url', 'alt']):
            return False, "Brakujące dane obrazu."
        if not img_data['url'].strip():
            return False, "Adres URL obrazu nie może być pusty."
        if not img_data['alt'].strip():
            return False, "Tekst alternatywny nie może być pusty."
        if not validators.url(img_data['url']):
            return False, "Niepoprawny format adresu URL obrazu."

    for field, error_msg in required_fields.items():
        if field not in data:
            return False, error_msg

    if not data['title'].strip():
        return False, "Tytuł nie może być pusty."
    if not data['desc'].strip():
        return False, "Opis nie może być pusty."
    if not data['text'].strip():
        return False, "Treść nie może być pusta."

    return True, ""
