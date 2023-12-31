import requests

from configuration import SERVICE_URL
from src.baseclasses.response import Response
from src.pydantic_schemas.post import Post


def test_getting_posts():
    """ Получение постов """
    r = requests.get(url=SERVICE_URL)
    response = Response(r)
    response.assert_status_code(200).validate(Post)
