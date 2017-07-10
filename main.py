import os
from configparser import ConfigParser
from ImageSave import ImageSave
from Upload import Upload

def read_config():
    conf = ConfigParser()
    conf.read(os.path.join(os.path.dirname(__file__), 'config.ini'))
    conf_dict = {}
    conf_dict['domain'] = conf.get('qiniu', 'domain')
    conf_dict['bucket'] = conf.get('qiniu', 'bucket')
    conf_dict['access_key'] = conf.get('qiniu', 'access_key')
    conf_dict['secret_key'] = conf.get('qiniu', 'secret_key')
    return conf_dict
 
if __name__=='__main__':
    img_path = ImageSave.image_save()
    if img_path:
        conf = read_config()
        upload2qiniu = Upload(conf, img_path)
        upload2qiniu.upload()