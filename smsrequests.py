import requests
from utils import default_header_user_agent
# 目标网站的API URL
url = "https://metaso.cn/verify?type=signup"

# 请求数据，这通常包括手机号码和其他必要的信息
payload = {
    "phone": "86-18398065530",      # 替换为目标号码
}

# 请求头，可能需要包含User-Agent或其他认证信息
headers = default_header_user_agent()

# 发送POST请求
response = requests.post(url, json=payload, headers=headers)

# 检查响应状态码和内容
if response.status_code == 200:
    print("SMS request successful!")
    print("Response:", response.json())
else:
    print(f"Failed to request SMS. Status code: {response.status_code}")
    print("Response:", response.text)
