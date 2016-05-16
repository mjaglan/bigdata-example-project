How To Run
===============================================================================

``Prerequisite:``
It is assumed following steps are already done - 

* cloud environment is setup.
* ``git clone --recursive https://github.com/futuresystems/big-data-stack.git`` in home directory
* load openstack module
* enable some cloud enviroment - india-futuresystems, or chameleon, or something else
* enable some virtual ennvironment
* install all the requirements from "big-data-stack"
* git clone this repository in the same home directory
* cd into `/src </src>`_


``installation:``

* run "source launch.sh" and wait until completion. this will do the job for you. After this, read msg on command line.  It will say - ::

    Please do following:
    ssh -i ~/.ssh/id_rsa <master0-ip-address> -l hadoop
    bash
    cd ~/twitter
    source main.sh

  To find ``<master0-ip-address>``, use ``nova list`` command.

* The analysis will end up showing the Sum Squared Error value related message.

Feel free to refer `video demo <https://youtu.be/PxM0yurCBPQ>`_ :)
