## 使用

给好友发送消息，需要添加机器人为好友；给群发消息，只需要将机器人拉进群里就好。

### Python

参考`wxbot_client_test.py`中的使用


### Matlab

1. 给`Mr. Xi`好友发消息

``` matlab
webwrite('http://192.168.1.129:5490/send-friend-msg', 'msg', 'test messages from matlab', 'to_user', 'Mr. Xi')
```

2. 给`业务通知群`发送消息

```matlab
webwrite('http://192.168.1.129:5490/send-group-msg', 'msg', 'test messages from matlab', 'to_group', '业务通知群')
```
