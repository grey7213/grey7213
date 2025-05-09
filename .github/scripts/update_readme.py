#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import re
import json
import random
import requests
from datetime import datetime
import pytz

def get_ascii_art():
    """返回酷炫的 ASCII Art"""
    # 可以替换为多个 ASCII Art，随机选择一个
    arts = [
        """   ____                     _   _      _  ____  _   
  / ___|_ __ __ _ _ __   __| | | | ___| |/ /  \\| |__  
 | |  _| '__/ _` | '_ \\ / _` | | |/ _ \\ ' /| | | '_ \\ 
 | |_| | | | (_| | | | | (_| | | |  __/ . \\| |_| | | |
  \\____|_|  \\__,_|_| |_|\\__,_| |_|\\___|_|\\_\\\\___/|_|_|
        grey7213  |  梦不见星空  |  0x67726579723133""",
        """
 /$$$$$$                               /$$   /$$ /$$$$$$  /$$  /$$  /$$
| $$__  $$                            | $$$ | $$|_  $$_/ | $$ | $$ | $$
| $$  \\__/  /$$$$$$   /$$$$$$  /$$   /$$$$$$| $$  | $$   | $$ | $$ | $$
| $$ /$$$$ /$$__  $$ /$$__  $$| $$  |_  $$_/| $$  | $$   |__/ |__/ |__/
| $$|_  $$| $$  \\__/| $$$$$$$$| $$    | $$  | $$  | $$                
| $$  \\ $$| $$      | $$_____/| $$    | $$ /| $$  | $$    /$$ /$$ /$$
|  $$$$$$/| $$      |  $$$$$$$| $$    |  $$$$/$$  /$$$$$$| $$| $$| $$
 \\______/ |__/       \\_______/|__/     \\___/|__/ |______/|__/|__/|__/
      ʕ•ᴥ•ʔ  梦不见星空 - 用代码创造未来  ʕ•ᴥ•ʔ"""
    ]
    return random.choice(arts)

def get_inspirational_quote():
    """获取一条随机名言警句"""
    try:
        response = requests.get("https://v1.hitokoto.cn/?c=d&encode=json")
        data = response.json()
        return f"🌟 {data['hitokoto']} —— {data.get('from_who', '佚名')}《{data.get('from', '未知')}》"
    except Exception as e:
        print(f"获取名言失败: {str(e)}")
        return "🌟 编程不仅仅是代码，更是一种思维。"

def get_current_time():
    """获取当前北京时间"""
    bj_tz = pytz.timezone('Asia/Shanghai')
    now = datetime.now(bj_tz)
    return now.strftime("%Y-%m-%d %H:%M:%S")

def update_readme():
    """更新 README.md 文件"""
    # 读取 README 文件
    readme_path = "README.md"
    
    if not os.path.exists(readme_path):
        print(f"找不到文件: {readme_path}")
        return False
    
    with open(readme_path, "r", encoding="utf-8") as file:
        readme_content = file.read()
    
    # 准备动态内容
    ascii_art = get_ascii_art()
    quote = get_inspirational_quote()
    current_time = get_current_time()
    
    # 构建动态内容
    dynamic_content = f"""<!-- 这里将由 GitHub Actions 自动更新 -->
```
{ascii_art}
```

{quote}

📅 最后更新时间: {current_time}"""
    
    # 使用正则表达式替换动态内容部分
    pattern = r"<!-- DYNAMIC_CONTENT_START -->.*?<!-- DYNAMIC_CONTENT_END -->"
    replacement = f"<!-- DYNAMIC_CONTENT_START -->\n{dynamic_content}\n<!-- DYNAMIC_CONTENT_END -->"
    new_readme = re.sub(pattern, replacement, readme_content, flags=re.DOTALL)
    
    # 写回文件
    with open(readme_path, "w", encoding="utf-8") as file:
        file.write(new_readme)
    
    print("README.md 更新成功!")
    return True

if __name__ == "__main__":
    update_readme() 