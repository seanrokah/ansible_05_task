# Ansible to setup application service on Linux based system

All applications run on Linux based systems with pre-determined service, which are essentially a process of the application created with `init.d` or `systemd`
We need to deploy the details_app to remote service with ansible playbook, while in the mean time, setting up the dependencies, verifying environment variables, installing the service and testing the endpoint remotely.

### Pre Requisits

- Remote Linux machine/VM
- Python3
- Ansible
- details_app access

### Tasks

- Create remote Linux machine/VM to setup the app on.
- Create ansible playbook that will:
    - Access remote machine
    - Get the application sources and place them appropriate location(suggested /home/details_app/ and also create user for the same application)
    - Setup application requirements (install requirements.txt or pyproject.toml)
    - Use pre-created service file to setup details_app on the remote machine/VM
    - Setup and verify that service is up
    - Reboot the remote machine/VM and check if the application is up and running by accessing the application directly

### Notes:

- In case you do not know how the service file should look, try checking other branches on the repository
- If you lack the knowledge of VMs, check with the instructor or RTFM
- All the playbook and config files need to be in seperate repo on your github/gitlab accounts
- Create README file with description of what does the playbooks do and how to set it up.
- While it is possible to work alone, don't hesitate to work in groups, and add CONTRIBUTION.md file to repository where each and everyone, writes his/her names and their contribution to the project