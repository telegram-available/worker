import os
import stat
import shutil
import _thread
import objects
from git.repo.base import Repo
# ========================================================================================================
stamp1 = objects.time_now()


def delete(action, name, exc):
    os.chmod(name, stat.S_IWRITE)
    os.remove(name)
    return action, name, exc


Repo.clone_from('https://github.com/evolvestin/Telegram-Username-Availability-Parser', 'temp')
shutil.copy('temp/test.py', 'functions.py')
shutil.rmtree('temp', onerror=delete)
# ========================================================================================================
print(f'Запуск за {objects.time_now() - stamp1} секунд(ы)')


if __name__ == '__main__':
    from functions import checking, files_upload
    _thread.start_new_thread(files_upload, ())
    checking()
