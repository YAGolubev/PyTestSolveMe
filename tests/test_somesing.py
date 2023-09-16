import requests

from configuration import SERVICE_URL
from src.baseclasses.response import Response
from src.schemas.user import User


def test_getting_users_list():
    response = requests.get(SERVICE_URL)
    # print(response.__getstate__())
    test_object = Response(response)
    test_object.assert_status_code(300).validate(User)
