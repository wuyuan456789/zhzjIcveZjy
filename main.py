import json
import requests

url = 'https://ark.cn-beijing.volces.com/api/v3/chat/completions'
h = {
    'Authorization': 'Bearer 你的token',
    'Content-Type': 'application/json',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36'
                  ' (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36',
}

d = {
    "model": "deepseek-v3-250324",  # deepseek-v3-250324   kimi-k2-250711  doubao-1-5-pro-32k-250115 doubao-1-5-lite-32k-250115
    "messages": [
        {"role": "user",
         "content": "你是一名无所不知的大学高材生，现在出一个“单选题”考考你，题目：“关于阴天光线叙述错误的是（ ）。”，选项数组（每个选项通过“###”相隔或者分割）：“[阴影面积小，不利于表现物体层次感###照度低、需补光###缺乏造型感、空间感###色温单一、易成统一色调]”。 告诉我正确答案，只需要返回选项数组里面的选项就行，不要任何解释和废话，简单简洁, 字数不能超过选项数组里面的。"
         }
    ],

}

# 根据选项数组里面的内容，告诉我每个选项正确的数字顺序（比如答案是DBCA应该返回4231），只需返回数字，每个数字通过“###”相隔或者分割，不要任何解释和废话，简单简洁

d = json.dumps(d).replace(' ', '')
r = requests.post(url=url, headers=h, data=d)
# print(r.json()['choices'][0]['message']['content'])
# print(r.json())
data_json = r.json()
print(data_json)