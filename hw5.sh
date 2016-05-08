script hw5-cmd.script -c "ansible-playbook site.yml -i inventory"
sleep 15
script -a hw5-cmd.script -c "ansible -m shell -a 'service mongodb status' -i inventory all -u ubuntu"
