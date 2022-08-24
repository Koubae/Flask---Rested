from copy import deepcopy
import traceback

API_RESPONSE_STRUCT = {
    'is_error': False,
    'code': None,
    'data': {

    },
    'errors': {
        'message': None,
        'error': None,
    }
}


def get_new_response() -> dict:
    """Creates a new http response object for json content-type

    Returns:
        dict:  deep-copy of the api response format
    """

    return deepcopy(API_RESPONSE_STRUCT)


def get_new_response_error(
        error_message: str = 'Internal Server Error',
        code: int = 500,
        error: any = None,
        data: dict = None
    ) -> dict:
    """

    Args:
        error_message (str):
        code (int):
        error (Exception):
        data (any):

    Returns:
        (dict) New Response dictionary set as error
    """
    response = get_new_response()
    response['is_error'] = True
    response['code'] = code
    response['errors']['message'] = error_message
    if error:
        try:
            response['errors']['error'] = ''.join(traceback.format_exception(None, error, error.__traceback__))
        except Exception as e:
            response['errors']['error'] = str(e)

    if data:
        response['data'] = data

    return response
