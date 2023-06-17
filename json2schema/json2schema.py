import json
from typing import Union

SCHEMA = 'http://json-schema.org/schema'


class JSON2Schema(object):
    def __init__(self, data: Union[str, dict, list], required_all=False, check_value=False):
        assert isinstance(data, str) or isinstance(data, dict) or isinstance(data, list), 'data仅支持str、dict、list'
        if isinstance(data, str):
            self._data = json.loads(data)
        else:
            self._data = data

        self.required_all = required_all
        self.check_value = check_value

    def _handle_null(self, data: None):
        schema = {'type': 'null'}
        if self.check_value is True:
            schema['pattern'] = '^null$'
        return schema

    def _handle_boolean(self, data: bool):
        schema = {'type': 'boolean'}
        if self.check_value is True:
            schema['pattern'] = '^%s$' % data
        return schema

    def _handle_number(self, data: float):
        schema = {'type': 'number'}
        if self.check_value is True:
            schema['pattern'] = '^%s$' % data
        return schema

    def _handle_integer(self, data: int):
        schema = {'type': 'integer'}

        if self.check_value is True:
            schema['pattern'] = '^%s$' % data
        return schema

    def _handle_string(self, data: str):
        schema = {'type': 'string'}
        if self.check_value is True:
            schema['pattern'] = '^%s$' % data
        return schema

    def _handle_object(self, data: dict):
        """处理object类型节点"""
        if not data:
            return {"type": "object"}
        schema = {"type": "object", 'properties': {key: self._handle_item(value) for key, value in data.items()}}
        if self.required_all:
            schema['required'] = list(data.keys())
        return schema

    def _handle_array(self, data: list):
        """处理object类型节点"""
        if not data:
            return {"type": "array"}
        schema = {"type": "array", 'items': [self._handle_item(item) for item in data[:1]]}
        return schema

    def _handle_item(self, data: Union[dict, list, int, float, bool, type(None)]):
        type_map = {
            int: self._handle_integer,
            float: self._handle_number,
            str: self._handle_string,
            list: self._handle_array,
            dict: self._handle_object,
            bool: self._handle_boolean,
            type(None): self._handle_null,
        }
        _handle_func = type_map.get(type(data))
        return _handle_func(data) if _handle_func else data

    def to_schema(self, title=None, description=None) -> dict:
        if not isinstance(self._data, (list, dict)):
            return {}

        schema = {
            "$schema": SCHEMA
        }
        if isinstance(title, str):
            schema['title'] = title
        if isinstance(description, str):
            schema['description'] = description

        schema.update(self._handle_item(self._data))
        return schema


def json2schema(data: Union[dict, list], required_all=True, check_value=False) -> Union[dict, list]:
    """
    change json to jsonschema
    :param data: the json data (as dict or list)
    :param required_all: mark all properties or items as required
    :param check_value: mark all value exact the same with the sample data
    :return:
    """
    return JSON2Schema(data, required_all=required_all, check_value=check_value).to_schema()
