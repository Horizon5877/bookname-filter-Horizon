# This is a sample Python script.
import json
# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import os

import unicodedata
from openai import OpenAI

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    client = OpenAI(
        # 若没有配置环境变量，请用百炼API Key将下行替换为：api_key="sk-xxx",
        api_key="sk-b960f2a86e0447389a17f0b3a0855963",
        base_url="https://dashscope.aliyuncs.com/compatible-mode/v1",
    )

    with open('书籍清单.txt', 'r', encoding='utf-8') as file:
        json_array = []
        for line in file:
            json_array.append(line.strip())
        jsonstring = json.dumps(json_array , ensure_ascii=False)
        print(jsonstring)

    completion = client.chat.completions.create(
        model="qwen-plus",
        messages=[
            {'role': 'system', 'content': '你是一个航天领域专家，你的使命是根据用户给出的书籍名称，判断其是否为航天领域的相关书籍'
                                          '示例输入1:'
                                          '书籍清单:[航天制导控制,航天系统工程,世界历史,高中英语]'
                                          '示例回答1:'
                                          '[航天制导控制,航天系统工程]'
             },
             {'role': 'user', 'content': '请帮我分析下面这个书籍名称清单中，哪些是航天领域书籍，无需给出思考过程'
                                         '书籍清单:'f'{jsonstring}'
             }
            ]
    )
    print(completion.choices[0].message.content)
    json_array = json.loads(completion.choices[0].message.content)

    with open('a.txt', 'w') as file:
        for item in json_array:
            file.write(item+'\n')
