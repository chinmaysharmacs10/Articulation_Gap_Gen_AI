import requests


class ImageUrlFetcher:
    def __int__(self):
        pass

    def get_image_url(self, product_id):
        OLD_URL = "img.fkcdn.com/image/"
        NEW_URL = "storage.googleapis.com/fk-p-image-"

        url = 'http://10.83.47.208/product/xif0q/' + product_id
        retry = 0
        r = requests.get(url=url)
        while r.status_code != 200 and retry < 5:
            retry += 1
            r = requests.get(url=url)

        if r.status_code == 200:
            try:
                r = r.json()
                img_url_0 = r['staticContentInfo']['staticcontents'][0]['transContents'][0]['attributeValues']['s3_path']['valuesList'][0]['value']
                img_url_0 = img_url_0.replace(OLD_URL, NEW_URL)
                return img_url_0
            except Exception as e:
                print("Exception: ", e)
                return None

        return None
