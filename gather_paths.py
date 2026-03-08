import contextlib
import os
import queue
import requests
import sys
import threading
import time
Filtered=[".jpg",".gif",".png",".css"]
target="http://boodelyboo.com/wordpress"
threads=10
answers=queue.Queue()
web_paths=queue.Queue()
def gather_paths():
    for root ,_, files in os.walk('.'):
        for fname in files:
            if os.path.splitext(fname)[1] in Filtered :
                continue
            path=os.path.join(root,fname)
            if path.startswith('.'):
                path=path[1:]
            print(path)
            web_paths.put(path)
@contextlib.contextmanager
def chdir(path):
    this_dir=os.getcwd()
    os.chdir(path)
    try:
        yield
    finally:
        os.chdir(this_dir)
if __name__=='__main__':
    with chdir("/home/kali/Downloads/wordpress"):
        gather_paths()
    input("Press return to continue.")
def test_remote():
    while not web_paths.empty():
        path=web_paths.get()
        url = f'{target}{path}'
        time.sleep(2)
        r=requests.get(url)
        if r.status_code:
            answers.put(url)
            sys.stdout.write('+')
        else:
            sys.stdout.write('x')
        sys.stdout.flush()