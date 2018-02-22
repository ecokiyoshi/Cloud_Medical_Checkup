# -*- coding:utf-8 -*-

import datetime


def unsupport_object_formatter(obj):
    #datetime->isoformat
    if isinstance(obj, datetime.datetime):
        return obj.isoformat()


if __name__ == '__main__':
    now_time = datetime.datetime.now()
    res = unsupport_object_formatter(now_time)
    print(res)
    print(type(res))

