# Copyright (c) 2020 Johnathan Kupferer
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)

from __future__ import (absolute_import, division, print_function)
__metaclass__ = type

ANSIBLE_METADATA = {
    'metadata_version': '1.1',
    'status': ['preview'],
    'supported_by': 'community'
}

from ansible.errors import AnsibleFilterError

def terraform_name_escape(name):
    return name.replace('.', '-')

# ---- Ansible filters ----
class FilterModule(object):

    def filters(self):
        return {
            'terraform_name_escape': terraform_name_escape
        }
