import logging
import os
from datetime import datetime
__name = 'inti logger'




def run(**data):
    logger = logging.getLogger('create_organization_package')
    logger.setLevel(logging.DEBUG)

    date = datetime.today().strftime('%Y%m%d')
    log_path = os.path.join(os.environ['PACKAGE_MAKER_PATH'], f'package_maker/log/{date}/create_organization_package.log')

    if not os.path.exists(os.path.dirname(log_path)):
        os.makedirs(os.path.dirname(log_path))
    file_handler = logging.FileHandler(log_path)
    formatter = logging.Formatter('%(asctime)s : %(levelname)s : %(name)s : %(message)s')
    file_handler.setFormatter(formatter)
    file_handler.setLevel(logging.DEBUG)
    logger.addHandler(file_handler)
    logger.info('------------------------------ init_logger ---------------------------------------')

    return 0, {
        'info': '',
        'return_data': {}
    }