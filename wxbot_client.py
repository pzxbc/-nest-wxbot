# -*- coding: utf-8 -*-


import requests

URL = 'http://192.168.1.129:5490/'


def send_friend_msg(msg, to_user):
    payload = {'msg': msg, 'to_user': to_user}
    r = requests.post(URL + 'send-friend-msg', data=payload)
    if r.status_code == requests.codes.ok:
        res = r.json()
        if res['success'] is True:
            return True
    return False


def send_group_msg(msg, to_group):
    payload = {'msg': msg, 'to_group': to_group}
    r = requests.post(URL + 'send-group-msg', data=payload)
    if r.status_code == requests.codes.ok:
        res = r.json()
        if res['success'] is True:
            return True
    return False
