'''
Created on Jun 21, 2017

@author: Gowtham

DEPRECATED

This is a hard coded version of generating yaml. 

'''
import logging
from string import lower
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

# create a file handler
handler = logging.FileHandler('./request.log')
handler.setLevel(logging.INFO)

# create a logging format
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
handler.setFormatter(formatter)

# add the handlers to the logger
logger.addHandler(handler)

DEFAULT_USER = 'admin'
DEFAULT_PASS = 'admin'
DEFAULT_PORT = '9083'
DEFAULT_HOSTNAME = '192.168.92.67'
check_mode=False
force=False
delete_runtime_interface_interface = '10.11.12.13'
delete_runtime_interface_port = '8080'
DEFAULT_LOG_LEVEL = 'DEBUG'
force = True
action = 'DELETE'


def create_isam_config_file():
    isam_config_file = './isam.yml'
    logger.info('Creating %s', isam_config_file)
    with open(isam_config_file, 'w+') as f:
#         f.write('  {kernel, [{net_ticktime,  %s}]},\n' % net_ticktime)
        f.write('- name: Delete Runtime Tuning Parameters\n')
        f.write('  isam:\n')
        f.write('    appliance: "%s"\n'  % DEFAULT_HOSTNAME)
        f.write('    username: "%s"\n'  % DEFAULT_USER)
        f.write('    password: "%s"\n'  % DEFAULT_PASS)
        f.write('    lmi_port: "%s"\n'  % DEFAULT_PORT)
        f.write('    log: "%s"\n'  % DEFAULT_LOG_LEVEL)
        f.write('    force: "%s"\n'  % force)
        f.write('    action: %s\n'  % get_action(action))
        f.write('    isamapi:\n')
        f.write('      interface:  "%s"\n'  % delete_runtime_interface_interface)
        f.write('      port:       "%s"\n'  % delete_runtime_interface_port)
        f.write('  when: delete_runtime_interface_interface is defined and delete_runtime_interface_port is defined \n')
        f.write('  notify: Commit Changes')

def get_action(method):
    switcher = {
        'delete': "ibmsecurity.isam.base.runtime.listening_interfaces.delete",
        'get': "ibmsecurity.isam.base.runtime.listening_interfaces.get",
        'create': "ibmsecurity.isam.base.runtime.listening_interfaces.create",
    }
    return switcher.get(lower(method), "nothing")

if __name__ == '__main__':

    create_isam_config_file()
