import os
import stat
import shutil
import objects
from git.repo.base import Repo
# ========================================================================================================
stamp1 = objects.time_now()


def delete(action, name, exc):
    os.chmod(name, stat.S_IWRITE)
    os.remove(name)
    return action, name, exc


Repo.clone_from('https://github.com/evolvestin/Telegram-Username-Availability-Parser/', 'temp')
for file_name in os.listdir('temp/worker'):
    shutil.copy(f'temp/worker/{file_name}', file_name)
shutil.rmtree('temp', onerror=delete)
# ========================================================================================================
print(f'Запуск оболочки за {objects.time_now() - stamp1} секунды')


if __name__ == '__main__':
    from functions import start
    start()
