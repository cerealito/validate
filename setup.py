import sys
from cx_Freeze import setup, Executable

path = sys.path + ['./src']

msi_options = {'add_to_path': False,
               'initial_target_dir': r'[ProgramFilesFolder]\%s\%s' % ('sogeti', 'validate')}

b_options = {'path': path,
             'compressed': True,
             'optimize': 2}

setup(name='validate',
      version='0.0.1',
      description='Test Case Validation',
      options={'build_exe': b_options,
               'bdist_msi': msi_options},
      executables=[Executable('validate.py', base='Win32GUI')])
