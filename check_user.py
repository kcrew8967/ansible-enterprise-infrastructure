#!/usr/bin/python
from ansible.module_utils.basic import AnsibleModule
import pwd

def main():
    module = AnsibleModule(
        argument_spec=dict(
            username=dict(type='str', required=True)
        )
    )
    user = module.params['username']

    try:
        pwd.getpwnam(user)
        module.exit_json(changed=False, msg="User exists", exists=True)
    except KeyError:
        module.exit_json(changed=False, msg="User does NOT exist", exists=False)

if __name__ == '__main__':
    main()
