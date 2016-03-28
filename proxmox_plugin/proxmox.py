"""Proxmox plugin for Let's Encrypt client"""
import re
import os
import subprocess
import logging
import zope.component
import zope.interface
from letsencrypt import interfaces
from letsencrypt.plugins import common
from shutil import copy
from os import chmod

logger = logging.getLogger(__name__)

class ProxmoxInstaller(common.Plugin):
    zope.interface.implements(interfaces.IInstaller)
    zope.interface.classProvides(interfaces.IPluginFactory)

    description = "Proxmox VE plugin for Let's Encrypt client"

    @classmethod
    def add_parser_arguments(cls, add):
        add("location", default="/etc/pve/local", help="Location of Proxmox VE certificates.")

    def prepare(self):
        pass  # pragma: no cover

    def more_info(self):
        return "Automatically deploy SSL certificate to Proxmox VE."

    def get_all_names(self):
        return []

    def deploy_cert(self, domain, cert_path=None, key_path, chain_path=None, fullchain_path=None):

        if not fullchain_path:
            raise errors.PluginError(
                "The proxmox plugin currently requires --fullchain-path to "
                "install a cert.")
        logger.info("Copy certificate")
#        f_cert = open(cert_path, 'r')
#        f_key = open(key_path, 'r')
#        f_fullchain = open(fullchain_path, 'r')

#        d_key = os.path.join(self.conf("location"),"pve-ssl.key")
#        d_fullchain = os.path.join(self.conf("location"),"pve-ssl.pem")

        copy(key_path, os.path.join(self.conf("location"),"pve-ssl.key"))
        copy(fullchain_path, os.path.join(self.conf("location"),"pve-ssl.pem"))

#        logger.info("Restore permission")


#        logger.info("Connect to databse %s" % printul_setting['mongodb_uri'])

#        f_cert.close()
#        f_key.close()

    def enhance(self, domain, enhancement, options=None):
        pass  # pragma: no cover

    def supported_enhancements(self):
        return []

    def get_all_certs_keys(self):
        return []

    def save(self, title=None, temporary=False):
        pass  # pragma: no cover

    def rollback_checkpoints(self, rollback=1):
        pass  # pragma: no cover

    def recovery_routine(self):
        pass  # pragma: no cover

    def view_config_changes(self):
        pass  # pragma: no cover

    def config_test(self):
        pass  # pragma: no cover

    def restart(self):
        def is_pid_1_systemd():
            try:
                cmdline = open('/proc/1/cmdline', 'rb').read(7)
                return cmdline.startswith('systemd')
            except IOError:
                return false

        def execute_command(command):
            logger.info("Executing command: %s" % command)
            try:
                proc = subprocess.Popen(command)
                proc.wait()

                if proc.returncode != 0:
                    logger.error("PVE API Proxy Server restart command returned an error")

            except (OSError, ValueError) as e:
                logger.error("Failed to execute the restart pveproxy command")

        if is_pid_1_systemd():
            logger.info("Using systemd to restart PVE API Proxy Server")
            unit_script_locations = ['/usr/lib/systemd/system/', '/etc/systemd/system/']
            pveproxy_service_names = ['pveproxy.service']
            for path in unit_script_locations:
                for name in pveproxy_service_names:
                    full_path = os.path.join(path, name)
                    if os.path.isfile(full_path):
                        logger.info("Found the PVE API Proxy Server file at %s" % full_path)
                        execute_command(['systemctl', 'restart', name])
                    return
            logger.error("Found systemd but not the PVE API Proxy Server so it could not be restarted")
        else:
            logger.info("Using init scripts and the service command to restart PVE API Proxy Server")
            init_script_names = ['pveproxy']
            for path in init_script_names:
                if os.path.isfile(os.path.join('/etc/init.d/', path)):
                    logger.info("Found the PVE API Proxy Server init script at %s" % path)
                    execute_command(['service', path, 'restart'])
                    return
            logging.error("Did not find the PVE API Proxy Server so it could not be restarted")
