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

To run the test playbook(s) in the tests/ directory:

  1. Install and start Docker.
  1. Run (from the role root directory) `distro=[distro] playbook=[playbook] ./tests/test.sh`

If you don't want the container to be automatically deleted after the test playbook is run, add the following environment variables: `cleanup=false container_id=$(date +%s)`

Uses test shim
    - `wget -O tests/test.sh https://gist.githubusercontent.com/geerlingguy/73ef1e5ee45d8694570f334be385e181/raw/`

