# Enterprise Infrastructure Automation via Ansible

## 📌 Project Overview
This repository contains a suite of Ansible playbooks and a custom Python module designed to automate the configuration, security, and deployment of a multi-node, cross-platform enterprise environment (Windows Server & Linux Ubuntu). 

By utilizing Infrastructure as Code (IaC), this project demonstrates the ability to rapidly provision users, enforce strict access controls, and deploy web services consistently without manual intervention.

## 🛠️ Technologies Used
* **Configuration Management:** Ansible
* **Operating Systems:** Windows Server 2022, Ubuntu Linux
* **Scripting:** Python, Bash, YAML
* **Web Services:** Microsoft IIS, Apache2
* **Identity & Security:** Active Directory / Local Users, Windows ACLs

## 📂 Key Capabilities Demonstrated

### 1. Windows Systems Administration & Security (`win_users.yml`, `win_acl.yml`)
* Automated the provisioning of local user accounts and departmental security groups.
* Configured advanced Access Control Lists (ACLs), disabling parent inheritance and enforcing principle-of-least-privilege modify rights for specific directories.

### 2. Custom Python Ansible Module (`check_user.py`, `verify_users.yml`)
* Developed a custom Python module integrating the `AnsibleModule` class and `pwd` library.
* Script automatically parses a `users.csv` file, cross-referencing requested accounts against the local Linux system to verify existence, drastically reducing manual auditing time.

### 3. Cross-Platform Web Server Deployment (`win_iis.yml`, `install_apache.yml`)
* Automated the installation and feature-configuration of Microsoft IIS on Windows nodes.
* Automated the deployment, caching, and startup of Apache2 web servers on Ubuntu nodes, including the automated pushing of localized `index.html` files.
