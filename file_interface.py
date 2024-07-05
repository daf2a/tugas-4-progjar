import os
import json
import base64
from glob import glob

class FileInterface:
    def __init__(self):
        os.chdir('files/')

    def list(self, params=[]):
        try:
            filelist = glob('*.*')
            return dict(status='OK', data=filelist)
        except Exception as e:
            return dict(status='ERROR', data=str(e))

    def get(self, params=[]):
        try:
            filename = params[0]
            if filename == '':
                return None
            with open(filename, 'rb') as fp:
                isifile = base64.b64encode(fp.read()).decode()
            return dict(status='OK', data_namafile=filename, data_file=isifile)
        except Exception as e:
            return dict(status='ERROR', data=str(e))
            
def upload(self, params=[]):
    if not params or len(params) < 2:
        return dict(status='ERROR', data='Invalid parameters')

    filename, encoded_file = params

    try:
        file_content = base64.b64decode(encoded_file)
        with open(filename, 'wb') as f:
            f.write(file_content)
        return dict(status='OK', data='File uploaded successfully')
    except Exception as e:
        return dict(status='ERROR', data=str(e))

def delete(self, params=[]):
    if not params or len(params) < 1:
        return dict(status='ERROR', data='Invalid parameters')

    filename = params[0]

    try:
        os.remove(filename)
        return dict(status='OK', data='File deleted successfully')
    except Exception as e:
        return dict(status='ERROR', data=str(e))


if __name__ == '__main__':
    f = FileInterface()