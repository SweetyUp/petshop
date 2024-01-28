# -*- coding: utf-8 -*-
import toml
import logging
import json
import time
import datetime
import copy
from tools import *
import cprint
import random

pet_synthesis_prompt = toml.load("./ai_api/prompt.toml")['pet_synthesis']
user_evaluate_prompt = toml.load("./ai_api/prompt.toml")['user_evaluate']
user_info =  toml.load("./ai_api/game_configs.toml")['user_info']
event_type_ls = toml.load("./ai_api/prompt.toml")['event_type_ls']

def get_pet(props_str):
    # global pet_synthesis_prompt
    pet_synthesis_prompt = toml.load("./ai_api/prompt.toml")['pet_synthesis']
    cprint.cprint.info('===========精灵孵化环节=========')
    # props_str = ''
    # if type(props_ls) == list:
    #     props_str = ','.join(props_ls) 
    # else:
    #     props_str = props_ls
    print('🧙魔法师放入了',props_str)
    print('🪄正在孵化小精灵')
    pet_synthesis_prompt = pet_synthesis_prompt.replace('{props}',props_str)
    pet_info = get_chatgpt_re(pet_synthesis_prompt,temperature=1.1)
    # pet_info = '可爱嘟嘟小精灵啊啊啊啊啊啊啊啊啊啊啊啊吃饭v个红包就能开门了，； 啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊'
    print('孵化成功！小精灵详细信息为：')
    print(pet_info)
    return pet_info


def get_evaluate(pet_info):
    user_evaluate_prompt = toml.load("./ai_api/prompt.toml")['user_evaluate']
    user_info =  toml.load("./ai_api/game_configs.toml")['user_info']
    event_type_ls = toml.load("./ai_api/prompt.toml")['event_type_ls']
    cprint.cprint.info('===========顾客评价环节=========')
    event_type = random.sample(event_type_ls,1)[0]
    print('🤔顾客正在思考评价')
    user_evaluate_prompt = user_evaluate_prompt.replace('{event_type}',event_type).replace('{pet_info}',pet_info).replace('{user_info}',user_info)
    user_evaluate = get_chatgpt_re(user_evaluate_prompt,temperature=1.1)
    print('顾客的评价为：')
    print(user_evaluate)
    try:
        user_evaluate_dict = json.loads(user_evaluate)
    except:
        user_evaluate_ls = [{"评分":"5星","评语":"系统默认好评"},{"评分":"1星","评语":"小精灵躲在蛋里不出来！差评！"}]
        user_evaluate_dict = random.sample(user_evaluate_ls,1)[0]
    return user_evaluate_dict



if __name__ == "__main__":
    # 测试函数
    user_input = ''
    props_ls = []
    print('咕噜咕噜～我是魔法锅，请放入你选择的材料🫧')
    while(user_input!='0'):
        user_input = input('')
        if user_input =='0':
            break
        props_ls.append(user_input)
    pet_info = get_pet(props_ls)
    user_evaluate_dict = get_evaluate(pet_info)





