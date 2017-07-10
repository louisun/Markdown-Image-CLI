import sys
import os
from qiniu import Auth, put_file

class Upload:
    def __init__(self, conf, img_path):
        self.img_path = img_path
        self.domain = conf.get('domain')
        self.bucket = conf.get('bucket')
        self.auth = Auth(access_key=conf.get('access_key'), secret_key=conf.get('secret_key'))
    
    def copy2clipboard(self, img_name):
        web_path = self.domain + '/' + img_name 
        markdown_img_path = '![]({})'.format(web_path)
        os.system("echo '{}' | xclip -selection clipboard".format(markdown_img_path))
    
    def upload(self):
        if self.auth:
            img_name = os.path.basename(self.img_path)
            token = self.auth.upload_token(bucket=self.bucket, key=img_name)
            ret, info = put_file(up_token=token, key=img_name, file_path=self.img_path)
            if ret.get('key')==img_name and img_name is not None:
                self.copy2clipboard(img_name)
                sys.exit()