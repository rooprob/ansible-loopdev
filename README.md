Ansible role for managing loopdisks
=======
Role Name
=========

Creates loopback disk via losetup on Linux.

Requirements
------------

losetup

Role Variables
--------------

A description of the settable variables for this role should go here, including any variables that are in defaults/main.yml, vars/main.yml, and any variables that can/should be set via parameters to the role. Any variables that are read from other roles and/or the global scope (ie. hostvars, group vars, etc.) should be mentioned here as well.

Array of loop device, disk image path and fs_type.

Dependencies
------------

TODO

Known Issues
------------

Only supports RHEL 6.

Raise PR for RHEL 7 (systemd integration), package differences with Debian, FreeBSD, NetBSD etc.

Example Playbook
----------------

Including an example of how to use your role (for instance, with variables passed in as parameters) is always nice for users too:

    - hosts: servers
      roles:
         - rooprob.loopdev

    losetup:
      - name: disk0
        device: /dev/loop0
        image: /var/disk0.img
        mode: "0600"
        owner: root
        group: root
        size: 128m

      - name: disk1
        device: /dev/loop1
        image: /var/disk1.img
        mode: "0600"
        owner: root
        group: root
        size: 2g

License
-------

MIT

Author Information
------------------

An optional section for the role authors to include contact information, or a website (HTML is not allowed).
