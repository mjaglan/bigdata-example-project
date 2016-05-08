import unittest
import os
import subprocess as sub
from lib import utils

subject = "hw3"
outputs = []

class HW3Test(unittest.TestCase):

    def test_1_openstack_module(self):
        p = sub.Popen(["nova", "--version"], stdout=sub.PIPE, stderr=sub.PIPE)
        output, errors = p.communicate()
        outputs.append(errors.rstrip())
        self.assertGreaterEqual(errors, 2.23)

    def test_2_credential(self):

        output = os.getenv("OS_TENANT_NAME")
        outputs.append(output)
        self.assertEqual(output, 'fg491')

    def test_3_default_key(self):
        home = os.getenv("HOME")
        res = os.path.exists(home+"/.ssh/id_rsa.pub")
        outputs.append(res)
        self.assertTrue(res)

    def test_4_key_registration(self):
        home = os.getenv("HOME")
        with open(home+"/.ssh/id_rsa.pub", "r") as f:
            fingerprint = utils.fingerprint_from_string(f.read())
            flist = utils.list_of_fingerprints()
            outputs.append(fingerprint)
            outputs.append(flist)
            self.assertIn(fingerprint, flist)

    def test_4_1_key_passphrase(self):
        pkey = os.getenv("HOME") + "/.ssh/id_rsa"
        p = sub.Popen(['grep', '-L', 'ENCRYPTED', pkey], stdout=sub.PIPE,
                stderr=sub.PIPE) 
        output, errors = p.communicate()
        if errors:
            outputs.append(errors.rstrip())
        else:
            outputs.append("ENCRYPTED")
        self.assertFalse(errors)

    def test_5_vm(self):
        vm_name = subject + "-" + os.getenv("OS_USERNAME")
        server = utils.find_server(vm_name)
        if server:
            global vm
            vm = server
            outputs.append(vm.name)
            vm_info = "ID, Name, Flavor, Image, Created: " + ", ".join([vm.id,
                vm.name, vm.flavor['id'], vm.image['id'], vm.created])
            outputs.append(vm_info)
        else:
            outputs.append("not found")
            outputs.append("not found")
        self.assertTrue(server)

    def test_6_vm_floating_ip(self):
        fip = utils.get_floating_ip(vm)
        outputs.append(fip)
        self.assertTrue(fip)

    def test_7_vm_SSH(self):
        ip = utils.get_floating_ip(vm)
        res = utils.call_ssh(ip)
        kname = res[0].rstrip()
        outputs.append(kname)
        self.assertEqual(kname, "Linux")

    def test_8_ansible(self):
        ip = utils.get_floating_ip(vm)
        res = utils.call_ssh(ip, cmd="which ansible")
        outputs.append(res[0].rstrip())
        self.assertTrue(res[0])

    def test_9_virtualenv(self):
        ip = utils.get_floating_ip(vm)
        res = utils.call_ssh(ip, cmd="which virtualenv")
        outputs.append(res[0].rstrip())
        self.assertTrue(res[0])
        
    def test_91_pip(self):
        ip = utils.get_floating_ip(vm)
        res = utils.call_ssh(ip, cmd="which pip")
        outputs.append(res[0].rstrip())
        self.assertTrue(res[0])

    @classmethod
    def tearDownClass(cls):
        with open(subject + '-results.txt','w') as f:
            for result in outputs:
                print>>f, result

if __name__ == '__main__':
    unittest.main()

