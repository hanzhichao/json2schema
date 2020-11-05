from json2schema import JSON2Schema, schema2list


def test_json2schema():
    data = {
        "args": {

        },
        "headers": {
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
            "Accept-Encoding": "gzip, deflate, br",
            "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6",
            "Host": "httpbin.org",
            "Sec-Fetch-Dest": "document",
            "Sec-Fetch-Mode": "navigate",
            "Sec-Fetch-Site": "none",
            "Sec-Fetch-User": "?1",
            "Upgrade-Insecure-Requests": "1",
            "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Safari/537.36 Edg/84.0.522.40",
            "X-Amzn-Trace-Id": "Root=1-5f257cbc-4cf1eda4ee64e61ba6902d20"
        },
        "origin": "111.202.190.36",
        "url": "https://httpbin.org/get",
        "abc": None
    }

    r = JSON2Schema(data).to_schema()
    print(r)


def test_schema2list():
    r = {
        "type": "object",
        "properties": {
            "retCode": {
                "type": "number",
                "description": ";@mock\u003d77847"
            },
            "retMsg": {
                "type": "string",
                "description": ";@mock\u003d测试内容p8m9"
            },
            "common": {
                "type": "array\u003cstring\u003e",
                "description": "常用分类;@mock\u003d$order(\u0027string1\u0027,\u0027string2\u0027,\u0027string3\u0027,\u0027string4\u0027,\u0027string5\u0027)"
            },
            "historical": {
                "type": "array\u003cstring\u003e",
                "description": "移除后的历史纪录;@mock\u003d$order(\u0027string1\u0027,\u0027string2\u0027,\u0027string3\u0027,\u0027string4\u0027,\u0027string5\u0027)"
            },
            "body": {
                "type": "object",
                "properties": {
                    "a": {"type": "string"}
                }
            }
        },
        "required": ['historical']
    }
    r = schema2list(r)
    print(r)
