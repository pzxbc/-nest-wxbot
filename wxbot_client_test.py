# -*- coding: utf-8 -*-

import wxbot_client


def test():
    wxbot_client.send_friend_msg('test_from_client', 'Mr. Xi')
    wxbot_client.send_group_msg('test_fromo_client', '业务通知群')


if __name__ == '__main__':
    test()
