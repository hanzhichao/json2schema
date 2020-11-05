class JSON2Schema(object):
    def __init__(self, data: dict):
        self._data = data

    def _handle_null(self, data: None):
        return {'type': 'null'}

    def _handle_boolean(self, data: bool):
        return {'type': 'boolean'}

    def _handle_number(self, data: float):
        return {'type': 'number'}

    def _handle_integer(self, data: int):
        return {'type': 'integer'}

    def _handle_string(self, data: str):
        return {'type': 'string', 'pattern': data}

    def _handel_object(self, data: dict):
        """处理object类型节点"""
        schema = {"type": "object"}
        schema['properties'] = {key: self._handle_item(value) for key, value in data.items()}  # todo
        return schema

    def _handel_array(self, data: list):
        """处理object类型节点"""
        schema = {"type": "array"}
        schema['items'] = [self._handle_item(item) for item in data[:1]]  # todo 严格模式
        return schema

    def _handle_item(self, data):
        type_map = {
            int: self._handle_integer,
            float: self._handle_number,
            str: self._handle_string,
            list: self._handel_array,
            dict: self._handel_object,
            bool: self._handle_boolean,
            type(None): self._handle_null,
        }
        _handle_func = type_map.get(type(data))
        return _handle_func(data) if _handle_func else data

    def to_schema(self):
        if not isinstance(self._data, (list, dict)):
            return {}

        schema = {"$schema": "http://json-schema.org/draft-04/schema#"}
        schema.update(self._handle_item(self._data))
        return schema


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
