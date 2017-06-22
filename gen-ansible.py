'''
Created on Jun 21, 2017

@author: Gowtham
'''
import logging
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

# create a file handler
handler = logging.FileHandler('/Users/sanju/request.log')
handler.setLevel(logging.INFO)

# create a logging format
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
handler.setFormatter(formatter)

# add the handlers to the logger
logger.addHandler(handler)

METHOD = 'DELETE'
DEFAULT_USER = 'admin'
DEFAULT_PASS = 'admin' 
check_mode=False
force=False

def create_isam_config_file():
    isam_config_file = '/Users/sanju/isam.config'
    logger.info('Creating %s', isam_config_file)
    with open(isam_config_file, 'w+') as f:
        f.write('[\n')
#         f.write('  {kernel, [{net_ticktime,  %s}]},\n' % net_ticktime)
        f.write('  {rabbit,\n')
        f.write('    [\n')
        f.write('     {loopback_users, []},\n')
        f.write('     {heartbeat, 580},\n')
        f.write('     {default_user, <<"%s">>},\n' % DEFAULT_USER)
        f.write('     {default_pass, <<"%s">>},\n' % DEFAULT_PASS)
#         f.write('     {default_vhost, <<"%s">>},\n' % default_vhost)
#         f.write('     {cluster_partition_handling, %s},\n' % cluster_partition_handling)
        f.write('     {cluster_nodes, {[\n')
#         if node_ips:
#             nodes_str = ','.join(["'rabbit@%s'" % get_node_name(n)
#                                   for n in node_ips])
#             f.write('      %s\n' % nodes_str)
        f.write('      ], disc}}\n')
        f.write('    ]\n')
        f.write('  },\n')
#         f.write('  {rabbitmq_management, [{listener, [{port, %s}]}]}\n'
#                 % rabbitmq_management_port)
        f.write('].\n')

if __name__ == '__main__':
    
    create_isam_config_file()