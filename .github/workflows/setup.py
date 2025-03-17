from setuptools import setup

APP = ['remove_transparency.py']  # 替换为你的Python脚本文件名
DATA_FILES = []
OPTIONS = {
    'argv_emulation': True,
    'packages': ['PIL'],  # 替换为你的依赖包
    'iconfile': './ico.ico'
}

setup(
    app=APP,
    data_files=DATA_FILES,
    options={'py2app': OPTIONS},
    setup_requires=['py2app'],
)
