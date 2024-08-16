import requests
import ddddocr

def ocr_space_file(filename, overlay=False, api_key='helloworld', language='eng'):
    """ OCR.space API request with local file.
        Python3.5 - not tested on 2.7
    :param filename: Your file path & name.
    :param overlay: Is OCR.space overlay required in your response.
                    Defaults to False.
    :param api_key: OCR.space API key.
                    Defaults to 'helloworld'.
    :param language: Language code to be used in OCR.
                    List of available language codes can be found on https://ocr.space/OCRAPI
                    Defaults to 'en'.
    :return: Result in JSON format.
    """

    payload = {'isOverlayRequired': overlay,
               'apikey': api_key,
               'language': language,
               }
    with open(filename, 'rb') as f:
        r = requests.post('https://api.ocr.space/parse/image',
                          files={filename: f},
                          data=payload,
                          )
    return r.content.decode()


def ocr_space_url(url, overlay=False, api_key='K85658807888957', language='eng'):
    """ OCR.space API request with remote file.
        Python3.5 - not tested on 2.7
    :param url: Image url.
    :param overlay: Is OCR.space overlay required in your response.
                    Defaults to False.
    :param api_key: OCR.space API key.
                    Defaults to 'helloworld'.
    :param language: Language code to be used in OCR.
                    List of available language codes can be found on https://ocr.space/OCRAPI
                    Defaults to 'en'.
    :return: Result in JSON format.
    """

    payload = {'url': url,
               'isOverlayRequired': overlay,
               'apikey': api_key,
               'language': language,
               }
    r = requests.post('https://api.ocr.space/parse/image',
                      data=payload,
                      )
    return r.content.decode(encoding='utf-8')


# Use examples:
test_url = ocr_space_url(url='https://e.3yit.com/captcha.html?0.8264300378482560', overlay=False, api_key='K85658807888957', language='eng')
print(type(test_url))
print(f"\n{test_url}")


def download_image(url, file_name):
    response = requests.get(url)
    with open(file_name,"wb")as file:
        file.write(response.content)
    print("图片下载成功！")
#调用下载函数
image_url = "https://e.3yit.com/captcha.html?0.8264300378482560"#图片的URL链接
file_name = "image.jpg" #保存的文件名
download_image(image_url, file_name)




ocr = ddddocr.DdddOcr()

image = open("image.jpg", "rb").read()
result = ocr.classification(image)
print(result)