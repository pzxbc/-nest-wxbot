# -*- coding: utf-8 -*-

import wxbot
import flask
from flask_restful import Resource, Api, reqparse
import itchat


app = flask.Flask(__name__)
api = Api(app)


class FriendMsgSender(Resource):
    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('msg')
        parser.add_argument('to_user')
        args = parser.parse_args()
        res = wxbot.send_friend_msg(args['msg'], args['to_user'])
        return {'success': res}


class GroupMsgSender(Resource):
    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('msg')
        parser.add_argument('to_group')
        args = parser.parse_args()
        res = wxbot.send_group_msg(args['msg'], args['to_group'])
        return {'success': res}


api.add_resource(FriendMsgSender, '/send-friend-msg')
api.add_resource(GroupMsgSender, '/send-group-msg')


def main():
    try:
        app.run(host='0.0.0.0', port=5490)
    except KeyboardInterrupt:
        if itchat.useHotReload:
            itchat.dump_login_status()


if __name__ == '__main__':
    main()

