import json
import os
import pathlib
from functools import lru_cache

import pandas
from quart import Quart, request
from quart_cors import cors

from apicategories import BASE_PROJECT, MEDIA_PATH, get_debug

ALLOWED_ORIGINS = [
    'http://localhost:3000'
]

app = Quart(__name__, root_path=BASE_PROJECT)
cors_app = cors(app, allow_credentials=True, allow_origin=ALLOWED_ORIGINS)

app.config.update(**{
    'SECRET_KEY': os.getenv('SECRET_KEY')
})


@cors_app.before_serving
def do_something():
    pass


@cors_app.before_request
def do_another():
    pass


@lru_cache(maxsize=100)
def read_json_file(path):
    if isinstance(path, pathlib.Path):
        if path.exists() and path.is_file():
            with open(path, mode='r', encoding='utf-8') as f:
                return json.load(f)
    return []


@cors_app.get('/categories/v1/')
async def categories():
    path = MEDIA_PATH.joinpath('categories.json')
    initial_data = read_json_file(path)
    return list(map(lambda x: x['title'], initial_data)), 200


@cors_app.get('/categories/v1/<category>')
async def subcategories(category):
    path = MEDIA_PATH.joinpath('categories.json')
    initial_data = read_json_file(path)

    items = list(
        filter(
            lambda x: x['title'] == category,
            initial_data
        )
    )

    if items:
        df = pandas.DataFrame(items[0]['subcategories'])
        return df.title.tolist(), 200
    return [], 200


if __name__ == '__main__':
    if get_debug():
        app.run(debug=get_debug())
    else:
        pass
