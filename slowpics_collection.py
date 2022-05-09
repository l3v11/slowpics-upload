import os
import requests
from requests_toolbelt import MultipartEncoder

# Uploads images to https://slow.pics/collection

path = "/path/to/images"

# =======================================

def slowpics_collection(path):
    img_list = os.listdir(path)

    data = {
        "collectionName": "Gallery",
        "hentai": "false",
        "optimizeImages": "false",
        "public": "false"
    }

    for i in range(0, len(img_list)):
        data[f"images[{i}].name"] = img_list[i]
        data[f"images[{i}].file"] = (img_list[i], open(f"{path}/{img_list[i]}", 'rb'), 'image/png')

    with requests.Session() as client:
        client.get('https://slow.pics/api/collection')
        files = MultipartEncoder(data)
        length = str(files.len)

        headers = {
            "Accept": "*/*",
            "Accept-Encoding": "gzip, deflate, br",
            "Accept-Language": "en-US,en;q=0.5",
            "Content-Length": length,
            "Content-Type": files.content_type,
            "Origin": "https://slow.pics/",
            "Referer": "https://slow.pics/collection",
            "Sec-Fetch-Mode": "cors",
            "Sec-Fetch-Site": "same-origin",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.88 Safari/537.36",
            "X-XSRF-TOKEN": client.cookies.get_dict()["XSRF-TOKEN"]
        }

        response = client.post("https://slow.pics/api/collection", data=files, headers=headers)

        return f"https://slow.pics/c/{response.text}"

# =======================================

print(slowpics_collection(path))
