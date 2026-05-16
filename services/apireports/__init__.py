import os
import pathlib
import dotenv

BASE_PROJECT = pathlib.Path(__file__).parent.absolute()

MEDIA_PATH = BASE_PROJECT / 'media'

if BASE_PROJECT.joinpath('.env'):
    dotenv.load_dotenv(BASE_PROJECT.joinpath('.env'))


def get_debug():
    value = os.getenv('DEBUG')
    return True if value == '1' else False
