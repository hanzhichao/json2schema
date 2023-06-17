class JSONSchema2List(object):
    def __init__(self, data: dict):
        self._data = data

    def _handle_object(self, data: dict):
        properties = data.get('properties')
        required = data.get('required')
        for key, value in properties.items():
            pass


def schema2list(data: dict, name=None, parent_data=None):
    required = data.get('required', [])
    if data.get('type') == 'object':
        items = data.get('properties', {})
    elif data.get('type') == 'array':
        items = data.get('items', {})
    else:
        return [dict(
            name=name,
            desc=data.get('description'),
            type=data.get('type') or 'string',
            example=data.get('type'),
            is_required=name in parent_data.get('required', []),
        )]
    result = []
    for name, value in items.items():
        item_data = dict(
            name=name,
            desc=value.get('description'),
            type=value.get('type') or 'string',
            example=value.get('type'),
            is_required=name in required,
        )
        if value.get('type') in ['object', 'array']:
            item_data['children'] = schema2list(value, name=name, parent_data=data)
        result.append(item_data)
    return result
