import os
import time
import random
import subprocess

DEFAULT_PATH = os.path.join(os.path.expanduser('~'), '.markdown_image')

# test if the content in clipboard is image
TEST_COMMAND = 'xclip -selection clipboard -t TARGETS -o'

SAVE_COMMAND = 'xclip -selection clipboard -t image/png -o > {}'

class ImageSave:
    '''
    Save the image from clipboard by using CLI tool xclip
    '''
    def __init__(self):
       pass 
    
    @classmethod
    def generate_path(self):
        '''
        Generate path based on current time
        '''
        if not os.path.exists(DEFAULT_PATH):
            os.mkdir(DEFAULT_PATH)
        file_num = int(
            os.popen('ls -l  ~/.markdown_image | grep "^-" |wc -l').read().strip())
        # remain the latest 20 imagetures
        if file_num > 20:
            os.system('rm ~/.markdown_image/*')
        time_str = time.strftime('%Y-%m-%d-%H-%M-%S', time.localtime(time.time()))
        return os.path.join(DEFAULT_PATH,
                            time_str + '_r' + str(random.randint(1, 100)) + '.png')
    @classmethod
    def image_save(self):
        '''
        Save the image from clipboard, return image path
        '''
        # test if the content in clipboard is image
        pipe_test = subprocess.Popen(TEST_COMMAND, shell=True, stdout=subprocess.PIPE)
        pipe_test.wait()

        if 'image' in pipe_test.stdout.read().decode('utf-8'):
            image_path = ImageSave.generate_path()
            pipe_save = subprocess.Popen(
                SAVE_COMMAND.format(image_path), shell=True, stderr=subprocess.PIPE)
            pipe_save.wait()
            # success to save the image
            if not pipe_save.stderr.read():
                return image_path
            else:
                return ''
        else:
            # text in clipboard, do nothing
            return ''