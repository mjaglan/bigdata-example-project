mypwd=$(pwd)

# STEP 1
cd "./../../big-data-stack/"
vcl boot -p openstack -P $USER-
#until $(ansible all -m ping); do 
#	sleep 30s
#done
sleep 300s
ansible-playbook play-hadoop.yml
ansible-playbook addons/spark.yml


# STEP 2
cd ${mypwd}
rm -rf "./../../big-data-stack/twitter"
mkdir  "./../../big-data-stack/twitter"
/bin/bash -c "cp twitter/* ./../../big-data-stack/twitter/"
ls "./../../big-data-stack/twitter"
cd "./../../big-data-stack/"
/bin/bash -c "ansible-playbook twitter/site.yml"


# STEP 3
echo "Please do following:"
echo "ssh -i ~/.ssh/id_rsa <master0-ip-address> -l hadoop"
echo "cd ~/twitter"
echo "source main.sh"
cd ${mypwd}
