import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


def test_disk_file(host):
    f = host.file('/var/disk0.img')

    assert f.exists
    assert f.user == 'root'
    assert f.group == 'root'


def test_losetup_command(host):
    with host.sudo():
        f = host.check_output('/sbin/losetup -a')

        assert f.startswith('/dev/loop0:')
        assert f.endswith('(/var/disk0.img)')
