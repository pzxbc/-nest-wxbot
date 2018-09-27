# -*- coding: utf-8 -*-

import os
import time


def stop_server(cmd):
    app = '"uwsgi --http :5490"'
    find_cmd = 'ps aux | grep '
    kill_cmd = cmd
    res = os.popen(find_cmd + app).readlines()
    for line in res:
        if 'grep' not in line:
            pid = line.split()[1]
            print(os.popen(kill_cmd + pid).read())


if __name__ == '__main__':
    kill_cmd = 'kill -2 '
    stop_server(kill_cmd)
    time.sleep(1)
    kill_cmd = 'kill -9 '
    stop_server(kill_cmd)
