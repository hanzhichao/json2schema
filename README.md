# json2schema

Get (Guess) jsonschema from one json sample

![example workflow](https://github.com/hanzhichao/json2schema/actions/workflows/python-app.yml/badge.svg)
[![](https://travis-ci.org/hanzhichao/json2schema.svg?branch=main)](https://travis-ci.org/hanzhichao/json2schema)
![](https://img.shields.io/badge/language-python-blue.svg)
![PyPI - Downloads](https://img.shields.io/pypi/dm/json2schema)
![PyPI - Python Version](https://img.shields.io/pypi/pyversions/json2schema)
![PyPI - License](https://img.shields.io/pypi/l/json2schema)



## Features

- json to jsonschema

## Install

```
$ pip install json2schema
```

## Use

### Simple Use

```python
from json2schema import json2schema
from pprint import pprint

data = {
    "first_name": "George",
    "last_name": "Washington",
    "birthday": "1732-02-22",
    "address": {
        "street_address": "3200 Mount Vernon Memorial Highway",
        "city": "Mount Vernon",
        "state": "Virginia",
        "country": "United States"
    }
}

schema = json2schema(data)
pprint(schema)

```
output

```shell
{'$schema': 'http://json-schema.org/schema',
 'properties': {'address': {'properties': {'city': {'type': 'string'},
                                           'country': {'type': 'string'},
                                           'state': {'type': 'string'},
                                           'street_address': {'type': 'string'}},
                            'required': ['street_address',
                                         'city',
                                         'state',
                                         'country'],
                            'type': 'object'},
                'birthday': {'type': 'string'},
                'first_name': {'type': 'string'},
                'last_name': {'type': 'string'}},
 'required': ['first_name', 'last_name', 'birthday', 'address'],
 'type': 'object'}
```

### More arguments

You can use `required_all=True` to mark all properties or items as required
with `schema = json2schema(data, required_all=True)` you will get 
```shell
{'$schema': 'http://json-schema.org/schema',
 'properties': {'address': {'properties': {'city': {'type': 'string'},
                                           'country': {'type': 'string'},
                                           'state': {'type': 'string'},
                                           'street_address': {'type': 'string'}},
                            'required': ['street_address',
                                         'city',
                                         'state',
                                         'country'],
                            'type': 'object'},
                'birthday': {'type': 'string'},
                'first_name': {'type': 'string'},
                'last_name': {'type': 'string'}},
 'required': ['first_name', 'last_name', 'birthday', 'address'],
 'type': 'object'}
```
or use `check_value=True` to mark all value exact the same with the sample data
with `schema = json2schema(data, check_value=True)`, you will get
```shell
{'$schema': 'http://json-schema.org/schema',
 'properties': {'address': {'properties': {'city': {'pattern': '^Mount Vernon$',
                                                    'type': 'string'},
                                           'country': {'pattern': '^United '
                                                                  'States$',
                                                       'type': 'string'},
                                           'state': {'pattern': '^Virginia$',
                                                     'type': 'string'},
                                           'street_address': {'pattern': '^3200 '
                                                                         'Mount '
                                                                         'Vernon '
                                                                         'Memorial '
                                                                         'Highway$',
                                                              'type': 'string'}},
                            'required': ['street_address',
                                         'city',
                                         'state',
                                         'country'],
                            'type': 'object'},
                'birthday': {'pattern': '^1732-02-22$', 'type': 'string'},
                'first_name': {'pattern': '^George$', 'type': 'string'},
                'last_name': {'pattern': '^Washington$', 'type': 'string'}},
 'required': ['first_name', 'last_name', 'birthday', 'address'],
 'type': 'object'}
 ```

## TODO:
- [ ] get jsonschema with multiple samples
- [ ] more args for json2schema