# -*- coding: utf-8 -*-

import wxbot
import os
import flask
from flask_restful import Resource, Api, reqparse
import werkzeug
import urllib

UPLOAD_FOLDER = os.path.join(
        os.path.dirname(os.path.abspath(__file__)), 'uploads')

app = flask.Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
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


class FileSender(Resource):
    def post(self):
        print(flask.request.form, flask.request.files)
        parser = reqparse.RequestParser()
        parser.add_argument('to_chat', location='form')
        parser.add_argument('file_name', location='form')
        parser.add_argument('url_encode', default='0', location='form')
        parser.add_argument(
                'file',
                type=werkzeug.datastructures.FileStorage,
                location='files'
                )
        args = parser.parse_args()
        if args['url_encode'] == '1':
            # url 解码
            # 专门针对matlab接口的
            # matlab库missing-http不能正常处理中文，所以转换成urlencode
            args['to_chat'] = urllib.parse.unquote(args['to_chat'])
            args['file_name'] = urllib.parse.unquote(args['file_name'])

        # file_name = werkzeug.utils.secure_filename(args['file'].filename)
        file_name = args['file_name']
        file_path = os.path.join(app.config['UPLOAD_FOLDER'], file_name)
        args['file'].save(file_path)
        res = True
        receiver = wxbot.get_receiver(args['to_chat'])
        if receiver:
            with wxbot.bot_lock:
                wxbot.core.send_file(file_path, receiver)
        return {'success': res}


api.add_resource(FriendMsgSender, '/send-friend-msg')
api.add_resource(GroupMsgSender, '/send-group-msg')
api.add_resource(FileSender, '/send-file')
