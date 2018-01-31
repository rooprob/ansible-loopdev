Ansible role for managing loopdisks

[![Build Status](https://travis-ci.org/rooprob/ansible-loopdev.svg?branch=master)](https://travis-ci.org/rooprob/ansible-loopdev)

loopdev
=========

Creates loopback disk via losetup on Linux.

Useful for additional disks without attaching real devices to your instance.

Requirements
------------

losetup

Role Variables
--------------

Array of loop device, disk image path and fs_type.

        losetup:
          - name: disk0
            device: /dev/loop0
            image: /var/disk0.img
            mode: "0600"
            owner: root
            group: root
            size: 10m


Known Issues
------------

None at this time.

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

Testing
-------

Building locally with Vagrant

        pip install -r requirements.txt
        molecule test

Requires Vagrant and VirtualBox, tested on MacOS High Sierra.

Travis
------

Travis supports the play execution only. The use of loop devices requires privileged access to the host. Travis doesn't support Vagrant.

-        ansible-galaxy install -r tests/requirements.yml -p tests/roles/
-        ansible-playbook -i tests/inventory tests/main.yml
