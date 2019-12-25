import json

from jsonpath_ng.ext import parse


def handle(event, context):
    print("input:" + json.dumps(event))

    result = {}

    forward = 'forward' in event

    print('forward field from input enabled?: {}'.format(forward))

    for key in sorted(event):
        try:
            if key.startswith('expression_'):
                field = key[11:]
                jsonpath_expr = parse(event[key])
                matches = jsonpath_expr.find(event)
                if matches and matches[0]:
                    result[field] = matches[0].value
            if key.startswith('unescape_'):
                field = key[9:]
                result[field] = json.loads(event[key])
            else:
                if forward:
                    result[key] = event[key]
        except:
            print('failed to process {}={}'.format(key, event[key]))

    return result
