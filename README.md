## 运行环境

需要Python3版本

```bash
python -m venv .env
source .env/bin/activate
pip install -r requirements.txt
```

## 使用

给好友发送消息，需要添加机器人为好友；给群发消息，只需要将机器人拉进群里就好。

### Python

参考`wxbot_client_test.py`中的使用


### Matlab

1\. 给`Mr. Xi`好友发消息

```matlab
webwrite('http://192.168.1.129:5490/send-friend-msg', 'msg', 'test messages from matlab', 'to_user', 'Mr. Xi')
```

2\. 给`业务通知群`发送消息

```matlab
webwrite('http://192.168.1.129:5490/send-group-msg', 'msg', 'test messages from matlab', 'to_group', '业务通知群')
```

3\. 发送文件

文件发送使用了`HTTP`的`multipart form`，但是2014版的`webwrite`不支持。最新版2018a提供了`matlab.net.http.io.MultipartFormProvider`用于支持`multipart form`操作


为了适应不同`matlab`版本，建议使用这个第三方库[missing-http](https://github.com/psexton/missing-http)


下载最新版的zip包: https://github.com/psexton/missing-http/releases, 然后解压

```matlab
run('path/to/missing-http/onLoad.m');
requestParts(1).Type = 'string';
requestParts(1).Name = 'to_chat';
requestParts(1).Body = urlencode('Nest业务通知群');
requestParts(2).Type = 'file';
requestParts(2).Name = 'file';
requestParts(2).Body = 'C:\Users\SUNNEST-OP\Documents\WeChat Files\gopzxbc\Files\test.jpg';
requestParts(3).Type = 'string';
requestParts(3).Name = 'file_name';
requestParts(3).Body = '中文测试.jpg';
requestParts(4).Type = 'string';
requestParts(4).Name = 'url_encode';
requestParts(4).Body = '1';
[statuscode, responsebody] = http.multipartPost('http://192.168.1.129:5490/send-file', requestParts)
```

## 使用CURL调试

建议使用`ChromeApp`中的`Postman`，可视化操作，不需要去查`Curl`的具体使用细则

1\. 模拟发送消息

```shell
curl http://127.0.0.1:5490/send-group-msg -d "msg=@Mr. Xi 测试&to_group=业务通知群" -X POST
```

2\. 模拟发送文件

```shell
curl -F "file=@/home/pzx/projects/nest-wxbot/test/27_130705105700_1.jpg" -F "to_chat=Nest业务通知群" -F "file_name=test.jpg" http://192.168.1.129:5490/send-file
```


## 开发中遇到的问题

1\. `requests`不能上传中文文件名的文件。修改`urllib3`目录下的`fields.py`文件的45行

```python
# value = '%s*=%s' % (name, value)
value = '%s="%s"' % (name, value)
```
