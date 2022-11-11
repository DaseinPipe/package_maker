import logging
import os

package_maker_dirpath = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
os.environ['PACKAGE_MAKER_PATH'] = package_maker_dirpath

log_path = os.path.join(package_maker_dirpath, 'package_maker/log/main.log')
logging.basicConfig(filename=log_path,
                    format='%(asctime)s %(message)s',
                    filemode='w')



