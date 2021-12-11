"""Main module."""
"""This module provides a simple netmiko example.  Example pyinstaller build commands are located
in the pyinstaller_build_files directory"""
import logging
import logging.config
import logging.handlers
import sys

import click
from netmiko import ConnectHandler
from netmiko.ssh_exception import (NetMikoAuthenticationException,
                                   NetMikoTimeoutException)

logger = logging.getLogger(__name__)


def add_two_numbers(arg1, arg2):
    if arg1 == 'blah':
        print('What?')
    return arg1 + arg2


def setup_logging(log_level,
                  logfile_name):
    """
    Simple logging example.  To reduce verbose logging, a lower level can be used.
    For example, using logging.WARNING would suppress notice, information, and debug logs

    :param log_level: Maximum Log level
    :param logfile_name: Log File name
    :return: None
    """
    logger.setLevel(log_level)
    # create formatter and add it to the handlers
    formatter = logging.Formatter(fmt='%(asctime)s %(levelname)-8s %(message)s',
                                  datefmt="%Y-%m-%dT%H:%M:%S%z")
    # file logs
    file_handler = logging.FileHandler(logfile_name)
    file_handler.setLevel(log_level)
    file_handler.setFormatter(formatter)

    # add the handlers to the logger
    logger.addHandler(file_handler)

    # console logs
    stream_handler = logging.StreamHandler()
    stream_handler.setLevel(log_level)
    stream_handler.setFormatter(formatter)
    logger.addHandler(stream_handler)


@click.command()
@click.option('--username', prompt='Username',
              help='Username with access to each host.',
              required=True)
@click.option('--password',
              prompt=True,
              hide_input=True,
              confirmation_prompt=True,
              required=True)
@click.option('--host-ip',
              prompt='Host IP',
              help='IP address to get show ver from',
              required=True)
@click.option('--port',
              prompt='SSH Port',
              prompt_required=False,
              help='SSH Port',
              default='22',
              required=False)
def main(username,
         password,
         host_ip,
         port):
    setup_logging(log_level=logging.DEBUG,
                  logfile_name='logging.txt')
    print(f'Username: {username}')
    print(f'Host IP: {host_ip}')
    print(f'SSH Port: {port}')

    # setup NTC templates directory

    if getattr(sys, 'frozen', False):
        # running in a bundle
        print('Running in a bundle.')
        parent_dir = sys._MEIPASS
    else:
        # assumes there is a templates subdirectory with the necessary files
        parent_dir = os.path.abspath('.')

    os.environ['NET_TEXTFSM'] = os.path.join(parent_dir, 'templates')

    cisco_device = {
        "device_type": "cisco_ios_ssh",
        "ip": host_ip,
        "username": username,
        "password": password,
        "port": port
    }

    logger.info(f'HOST:{host_ip:15} Connecting on port {port} using SSH:')

    try:
        cisco_ssh = ConnectHandler(**cisco_device)
        versions = cisco_ssh.send_command("show version", use_textfsm=True)
        hostname = versions[0]['hostname']
        version = versions[0]['version']
        logger.info(f"HOST:{host_ip:15} Hostname: {hostname} Version: {version}.")
        cisco_ssh.disconnect()
    except NetMikoTimeoutException:
        logger.error(f"HOST:{host_ip:15} Timeout error occurred.")
        sys.exit(1)
    except NetMikoAuthenticationException:
        logger.error(f"HOST:{host_ip} Authentication error occurred.")
        sys.exit(1)
    except Exception as exc:
        logger.error(f"HOST:{host_ip} Unknown error occurred. {str(exc)}")
        sys.exit(1)


if __name__ == '__main__':
    main()
