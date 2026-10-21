import json

import jsonschema

from common.baserequest import logger


def check_schema(res,schemaPath):
    try:
        with open(schemaPath) as f:
            schema = json.load(f)
        jsonschema.validate(res,schema)
    except jsonschema.exceptions.ValidationError as e:
        logger.error(e)
        return False
    else:
        return True