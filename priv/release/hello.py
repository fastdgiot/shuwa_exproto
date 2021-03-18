# coding=utf8
import os
import requests

s = requests.session()

def post(args,session,env):
    #body = json.loads(base64.b64decode(args).decode("utf-8"))
    #print(body)
    #strbody = '{}'.format(body)
    #enbody =  base64.b64encode(strbody.encode('utf-8'))
    #print(enbody)
    #state = json.loads(base64.b64decode(env).decode("utf-8"))
    #print(state)
    # resturl = state['roles'][0]['tag']['appconfig']['rest']
    # print(resturl)
    # s.headers.update({"sessionToken": session, 'Content-Type': 'application/json'})
    # rt = s.get('{}/classes/Device?order=createdAt&limit=10&skip=0'.format(resturl),
    #              params={'order': 'createdAt', })
    # for row in (rt.json()['results']):
    #     print(row)
    Url = 'http://124.156.153.59:3000/d/9CWBz0bik/zetaya-ce-jian-kong?tab=query&editPanel=199&from=now-30m&orgId=1&to=now&var-device=All&var-hostname=All&var-job=shuwa_node&var-maxmount=%2F&var-node=124.156.153.59:9100&var-show_hostname=VM-16-11-centos&Authorization=Bearer eyJrIjoia0Y0dEg4Mzg1OFdhZThEQU85NzRwZ0hQNHpLNEtZOWEiLCJuIjoiemV0YSIsImlkIjoxfQ=='
    rt = s.get(Url,
               params={})
    print(rt.content)
    print(args)
    print(session)
    print(env)
    return args

def main():
    #{"name":"shuwa"}
    argvs = 'eyJuYW1lIjoic2h1d2EifQ=='


    return  post(argvs, 'session','env')

def exit():
    os._exit(0)

if __name__ == "__main__":
    main()