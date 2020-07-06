#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
通知脚本loonflow会将标题、内容、参与人等信息作为全局变量传给通知脚本，脚本中直接使用这些参数，通过各自的发送消息逻辑将信息发送出去。
详情参数参考：loonflow/media/notice_script/demo_notice_script.py 里面有变量名称。
本脚本引用三个变量：participant：接收人，content_result：内容，title_result：标题,ticket_value_info:包含creator、sn等信息。
另外通知脚本内容是exec来执行的，不是直接执行脚本。所以 __name__ !== "__main__"，不能用if __name__ == "__main__"。
"""

import json
import requests

class WeChat:
    def __init__(self):
        self.CORPID = '******'
        self.CORPSECRET = '*******************************'
        self.AGENTID = '1000020'

    def _get_access_token(self):
        url = 'https://qyapi.weixin.qq.com/cgi-bin/gettoken'
        values = {'corpid': self.CORPID,
                  'corpsecret': self.CORPSECRET,
                  }
        req = requests.post(url, params=values)
        return req

    def get_access_token(self):
        get_req = self._get_access_token()
        if get_req.status_code != 200:
            print('连接服务器失败')
        else:
            get_req_json = json.loads(get_req.text)
            if get_req_json['errcode'] != 0:
                print('响应结果不正确')
            else:
                access_token = get_req_json['access_token']
                return access_token

    def get_ticket_sn(self):
        """
        ticket_value_info = {'id': 34, 'creator': 'test', 'gmt_created': '2019-11-05 02:25:17',
                             'gmt_modified': '2019-11-05 02:26:38',
                             'is_deleted': False, 'title': '', 'workflow_id': 3, 'sn': 'loonflow_201911050002',
                             'state_id': 16,
                             'parent_ticket_id': 0, 'parent_ticket_state_id': 0, 'participant_type_id': 1,
                             'participant': 'weave',
                             'relation': 'weave', 'in_add_node': False, 'add_node_man': '',
                             'script_run_last_result': True,
                             'is_end': False, 'is_rejected': True, 'multi_all_person': '{}', 'jllx': '1', 'zjjl': 'www',
                             'jlz': '172.16.1.1', 'sm': 'aaaaaaaaaaaa', 'ym': '1'}
        :return:
        """
        for k_sn, v_sn in ticket_value_info.items():
            if k_sn == 'sn':
                return v_sn

    def get_ticket_creator(self):
        for k_creator, v_creator in ticket_value_info.items():
            if k_creator == 'creator':
                return v_creator

    def send_data(self):
        send_url = 'https://qyapi.weixin.qq.com/cgi-bin/message/send?access_token=' + self.get_access_token()
        ticket_sn = self.get_ticket_sn()
        ticket_creator = self.get_ticket_creator()
        send_values = {
            "touser": participant,
            "msgtype": "text",
            "agentid": self.AGENTID,
            "text": {
                "content": '您收到新的工单，请及时处理！\n申请人：%s \n工单号：<a href=\"http://workflow.wmqhealth.com/ticket/todo\">%s</a>' % (ticket_creator,ticket_sn)
            },
            "safe": "0"
        }
        send_msges = (bytes(json.dumps(send_values), 'utf-8'))
        respone = requests.post(send_url, send_msges)
        respone = respone.json()
        return respone["errmsg"]


wx = WeChat()
wx.send_data()
