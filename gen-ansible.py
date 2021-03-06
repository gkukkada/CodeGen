'''
Created on Jun 21, 2017

@author: Gowtham
'''
import logging
from string import lower
import yaml
import pprint, warnings
from jinja2 import Template, FileSystemLoader,Environment

templateLoader = FileSystemLoader( searchpath="./templates" )
templateEnv = Environment( loader=templateLoader )
TEMPLATE_FILE = "delete.yaml"


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

DEFAULT_USER = 'admin@local'
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
isam_config_file = './isam.yml'
isam_config_template = 'templates/delete.yaml'

def create_isam_config_file():
    warnings.warn(
        'create_isam_config_file() is deprecated, use create_isam_yml() instead', DeprecationWarning,stacklevel=2)
    logger.info('Creating %s', isam_config_file)
    arr = []
    data={}
    data['name'] = 'Delete Runtime Tuning Parameters'
    data['isam'] = {}
    data['isam']['appliance'] = DEFAULT_HOSTNAME
    data['isam']['username'] = DEFAULT_USER
    data['isam']['password'] = DEFAULT_PASS
    data['isam']['lmi_port'] = DEFAULT_PORT
    data['isam']['log'] = DEFAULT_LOG_LEVEL
    data['isam']['force'] = force
    data['isam']['action'] = get_action(action)
    data['isam']['isamapi']={}
    data['isam']['isamapi']['interface'] = delete_runtime_interface_interface
    data['isam']['isamapi']['port'] = delete_runtime_interface_port
    data['when'] = 'delete_runtime_interface_interface is defined and delete_runtime_interface_port is defined'
    data['notify'] = 'Commit Changes'
    arr.append(data)
    logger.info('Final yaml \n %s', yaml.dump(arr,default_flow_style=False,indent=4))

    with open(isam_config_file, 'w+') as f:
        yaml.safe_dump(arr,f, allow_unicode=True, encoding='utf-8', default_flow_style=False, indent=4)


def create_isam_yml():
        logger.info('Creating %s', TEMPLATE_FILE)
        template = templateEnv.get_template( TEMPLATE_FILE )
        output = template.render(
            action=get_action(action),
            appliance=DEFAULT_HOSTNAME,
            force=force,
            interface=delete_runtime_interface_interface,
            port=delete_runtime_interface_port,
            lmi_port=delete_runtime_interface_port
        )
        with open(isam_config_file, 'w+') as f:
            logger.info('Final yaml \n %s', output)
            f.write(output)

def get_action(method):
    switcher = {
        'delete': "ibmsecurity.isam.base.runtime.listening_interfaces.delete",
        'get': "ibmsecurity.isam.base.runtime.listening_interfaces.get",
        'create': "ibmsecurity.isam.base.runtime.listening_interfaces.create",
    }
    return switcher.get(lower(method), "nothing")

if __name__ == '__main__':

    logger.info('>> create_isam_yml')
    create_isam_yml()
    logger.info('<< create_isam_yml')
