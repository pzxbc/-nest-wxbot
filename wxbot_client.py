# -*- coding: utf-8 -*-

import os
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


def send_job_group_msg(msg):
    return send_group_msg(msg, 'Nest业务通知群')


def send_file(file_path, to_chat):
    files = {
            'file': open(file_path, 'rb'),
            'to_chat': (None, to_chat),
            # requests.post不能正常post中文文件名的文件
            # 手动添加一个文件名字段，服务端用此字段
            'file_name': (None, os.path.basename(file_path))}

    r = requests.post(URL + 'send-file', files=files)
    if r.status_code == requests.codes.ok:
        res = r.json()
        if res['success'] is True:
            return True
    return False
