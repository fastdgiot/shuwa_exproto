# coding=utf8
import os
import requests
import paho.mqtt.client as mqtt
import base64

s = requests.session()
mqttclient = None
mqttclinetid = "clinetid"

def on_connect(client, userdata, flags, rc):
    print("Connected with result code: " + "{}".format(rc) )

def on_message(client, userdata, msg):
    print(msg.topic + " " + "{}".format(msg) )

def printf(payload):
    global mqttclient
    global mqttclinetid
    if mqttclient == None:
        mqttclient = mqtt.Client(mqttclinetid, clean_session=True, userdata=None, protocol=3, transport="tcp") #指定mqtt协议为3.1版本，满足模糊匹配需求
        mqttclient.username_pw_set('shuwalog', password="session")
        mqttclient.on_connect = on_connect
        mqttclient.on_message = on_message
        mqttclient.connect('127.0.0.1', 1883, 60)
        mqttclient.loop_start()
    # client.subscribe('#', qos=0)  #订阅的topic
    strbody = '{}'.format(payload)
    enbody =  base64.b64encode(strbody.encode('utf-8'))
    mqttclient.publish(mqttclinetid, '{}'.format(enbody))
    print(payload)

def post_before(session):
    global mqttclinetid
    mqttclinetid = session
    printf("init")

def post_after():
    global mqttclinet
    mqttclinet.disconnect()

def post(args, session, env):
    post_before(session)

    # body = json.loads(base64.b64decode(args).decode("utf-8"))
    # print(body)
    # strbody = '{}'.format(body)
    # enbody =  base64.b64encode(strbody.encode('utf-8'))
    # print(enbody)
    # state = json.loads(base64.b64decode(env).decode("utf-8"))
    # print(state)
    # resturl = state['roles'][0]['tag']['appconfig']['rest']
    # print(resturl)
    # s.headers.update({"sessionToken": session, 'Content-Type': 'application/json'})
    # rt = s.get('{}/classes/Device?order=createdAt&limit=10&skip=0'.format(resturl),
    #              params={'order': 'createdAt', })
    # for row in (rt.json()['results']):
    #     print(row)
    Url = 'http://124.156.153.59:3000/d/9CWBz0bik/zetaya-ce-jian-kong?tab=query&editPanel=199&from=now-30m&orgId=1&to=now&var-device=All&var-hostname=All&var-job=shuwa_node&var-maxmount=%2F&var-node=124.156.153.59:9100&var-show_hostname=VM-16-11-centos&Authorization=Bearer eyJrIjoia0Y0dEg4Mzg1OFdhZThEQU85NzRwZ0hQNHpLNEtZOWEiLCJuIjoiemV0YSIsImlkIjoxfQ=='
    rt = s.get(Url, params={})
    printf(rt.content)
    printf(args)

    post_after()
    return args


def main():
    # {"name":"shuwa"}
    argvs = 'eyJuYW1lIjoic2h1d2EifQ=='
    return post(argvs, 'session', 'env')

def exit():
    os._exit(0)


if __name__ == "__main__":
    main()
