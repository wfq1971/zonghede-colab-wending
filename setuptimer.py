import os, shutil
curdir = os.path.dirname(os.path.realpath(__file__))
os.makedirs('/common/cswpf/static', exist_ok=True)
timerscriptdir = '/common/cswpf/extensions-builtin/nocrypt-colab-timer/javascript'
os.makedirs(timerscriptdir, exist_ok=True)
timerscriptpath = os.path.join(timerscriptdir, 'colab-timer.js')
if not os.path.exists(timerscriptpath):
    shutil.copy2(os.path.join(curdir, 'colab-timer.js'), os.path.join(timerscriptpath))
