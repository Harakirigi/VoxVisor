import requests

def search_image(image_bytes):
    url = "https://api.tineye.com/rest/search/"
    files = {'image': image_bytes}
    headers = {'Api-Key': 'YOUR_TINEYE_API_KEY'}

    response = requests.post(url, files=files, headers=headers)
    
    if response.status_code == 200:
        return response.json()
    else:
        return {"error": "Не удалось выполнить поиск"}
