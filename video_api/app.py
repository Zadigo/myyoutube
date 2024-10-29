import json
import os
import pathlib
from functools import lru_cache

from quart import Quart, jsonify
from quart_cors import cors

from video_api import BASE_PROJECT, MEDIA_PATH, get_debug

app = Quart(__name__, root_path=BASE_PROJECT)
app = cors(app, allow_credentials=True, allow_origin=[
    'http://localhost:5173'
])

app.config.update(**{
    'SECRET_KEY': os.getenv('SECRET_KEY')
})


@app.before_serving
def do_something():
    pass


@app.before_request
def do_another():
    pass


@lru_cache(maxsize=100)
async def read_json_file(path):
    if isinstance(path, pathlib.Path):
        if path.exists() and path.is_file():
            with open(path, mode='r', encoding='utf-8') as f:
                return json.load(f)
    return []


@app.get('/api/v1/categories')
async def categories():
    path = MEDIA_PATH.joinpath('categories.json')
    initial_data = await read_json_file(path)
    data = map(lambda x: x['title'], initial_data)
    return jsonify(list(data))


@app.get('/api/v1/categories/<category>')
async def subcategories(category):
    path = MEDIA_PATH.joinpath('reports.json')
    categories = await read_json_file(path)
    selected_categories = filter(
        lambda x: x['title'] == category,
        categories
    )
    subcategories = map(lambda x: x['subcategories'], selected_categories)
    return jsonify(list(subcategories))


@app.get('/api/v1/reports')
async def reports():
    path = MEDIA_PATH.joinpath('reports.json')
    return jsonify(read_json_file(path))


if __name__ == '__main__':
    if get_debug():
        app.run(debug=get_debug())
    else:
        pass
