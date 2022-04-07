#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @FileName     :   json2schema.py
# @Author       :   superhin
# @CreateTime   :   2022/3/28 12:21
# @Function     :
import json
import os
from pprint import pprint
from typing import Union


class JSON2Schema(object):
    def __init__(self, data: Union[str, dict, list], required_all=True, check_value=False):
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

    def to_schema(self, title=None, description=None)->str:
        if not isinstance(self._data, (list, dict)):
            return "{}"

        schema = {
            "$schema": "http://json-schema.org/draft-04/schema#"
        }
        if isinstance(title, str):
            schema['title'] = title
        if isinstance(description, str):
            schema['description'] = description
            
        schema.update(self._handle_item(self._data))
        return json.dumps(schema, ensure_ascii=False)


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


if __name__ == '__main__':
    path = '/Users/superhin/Projects/chainmaker-sdk-python/tests/schemas/objects'
    for file in os.listdir(path):
        with open(os.path.join(path, file)) as f:
            data = json.load(f)
            print(data)
            schema = JSON2Schema(data).to_schema(title='TransactionInfo', description='交易信息')
        base_name = os.path.basename(file).strip('.json')
        output_file_name = f'{base_name}Schema.json'
        with open(os.path.join(os.path.dirname(path), 'schemas', output_file_name), 'w') as f:
            f.write(schema)
    # pprint(schema)
    # schema = json.dumps(schema, indent=2, ensure_ascii=False)
    # print(schema)
