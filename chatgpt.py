# -*- coding: utf-8 -*-

import poai
def chatgpt(question):
    result = poai.chatgpt.chat(api_key='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', prompt = question)
    with open("result.txt","w+",encoding="utf-8") as result1:
        result1.write(result)
if __name__ == '__main__':
    while True:
        print("空闲时候欢迎您进入越剧欣赏：https://mp.weixin.qq.com/s/JlmEvfWS6Pv1_3lqQ47Hkg")
        chatgpt(question=input("我是机器人ChatGPT，请输入您要咨询的问题:"))
        q = input("聊天请继续或回车，退出请输入：q")
        if "q" == q:
            break