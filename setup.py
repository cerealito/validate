import sys
from cx_Freeze import setup, Executable

path = sys.path + ['./src']

b_options = {'path': path,
             'compressed': True,
             'optimize': 2,
             'icon': './ui/icons/account-logged-in.ico'}

setup(name='validate',
      version='0.0.1',
      description='Test Case Validation',
      options={'build_exe': b_options},
      executables=[Executable('validate.py', base='Win32GUI')])
