from setuptools import setup

APP = ['remove_transparency.py']  # 入口脚本文件名
DATA_FILES = []
OPTIONS = {
    'argv_emulation': True,
    'packages': ['PIL'],  # 依赖包（Pillow 的包名是 PIL）
}

setup(
    app=APP,
    data_files=DATA_FILES,
    options={'py2app': OPTIONS},
    setup_requires=['py2app'],
)
