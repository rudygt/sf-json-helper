import json

from jsonpath_ng.ext import parse

FORWARD_KEY = '_forward'


def handle(event, context):
    print("input r:" + json.dumps(event))

    result = {}

    forward = FORWARD_KEY in event

    print('forward field from input enabled?: {}'.format(forward))

    for key in sorted(event):
        try:
            if key.startswith('expression_'):
                field = key[11:]
                jsonpath_expr = parse(event[key])
                matches = jsonpath_expr.find(event)
                if matches and matches[0]:
                    result[field] = matches[0].value
                continue

            if key.startswith('unescape_'):
                field = key[9:]
                result[field] = json.loads(event[key])
                continue

            if forward and key != FORWARD_KEY:
                result[key] = event[key]
        except:
            print('failed to process {}={}'.format(key, event[key]))

    return result
