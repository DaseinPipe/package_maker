#!/usr/bin/python3

import os, sys
package_maker_dirpath=os.path.dirname(os.path.realpath(__file__))


if package_maker_dirpath not in sys.path:
    sys.path.append(package_maker_dirpath)

from package_maker.src.config.config_main import *
from package_maker.src.utils import general_utils

def select_user_input(choice_list):
  user_text = 'Pick one: '
  for index, each in enumerate(choice_list):
    user_text += f'{index+1}) {each} | '
  result = ''
  while True:
    user_input = input(user_text)
    if user_input == 'break':
      exit()
    elif not user_input.isdigit():
      print(f'Type a number 1-{len(choice_list)}')
      continue
    elif int(user_input) not in range(1, len(choice_list)+1):
      print(f'Type a number 1-{len(choice_list)}')
      continue
    else:
      result = choice_list[int(user_input)-1]
      break
  return result

def select_folder(title):
  from PySide2.QtWidgets import QFileDialog, QApplication
  if not QApplication.instance():
    app = QApplication(sys.argv)
  else:
    app = QApplication.instance()

  directory = QFileDialog.getExistingDirectory(caption=title)
  app.quit()
  return directory

def confirm_data():
  while True:
    user_input = input('Please confirm above data before proceeding, y|n > ')
    if user_input == 'break':
      exit()
    elif user_input not in ['y', 'n']:
      print(f'Type a letter y or n')
      continue
    elif user_input == 'y':
      break
    else:
      exit()


global_data = get_global_data()
destination_list = list(global_data['destination'].keys())
vendor = select_user_input(destination_list)

job_list = list(global_data['destination'][vendor]['job'].keys())
job = select_user_input(job_list).lower()

print('Please Select Source Folder')
sourc_path = select_folder(title='Select source Folder')
print(f'Source Folder: {sourc_path}')

print('Please Select Destination Folder')
destination_path = select_folder(title='Select destination Folder')
print(f'destination Folder: {destination_path}')

data = dict(
  source_dir_path=sourc_path,
  destination_dir_path=destination_path,
  job=job,
)



print('---------- package started-------------')
general_utils.process_executor(
    project=job,
    processor='create_organization_package',
    process='discipline',
    data=data,
)





