# Docker Task
Our goal in this task was to containarize a *flask* application and its database using **Docker**.And run an automated proccess of running the whole application using **Ansible**

## How To run
Follow these steps to run this application:
1.  Install git on your device 
`yum install get`
2. Make a directory and clone this repository 
`makedir <directory name>`
`git clone "https://github.com/ImadAker/docker_task"`
3. Make sure Ansible is installed (if not use:`yum install epel-release ansible` )
4. Run the app 
`ansible-playbook -i inventory.txt playbook.yml`

5.The flask application should be running and heres how to use it
    1. To get cpu percentages over the last 24 hours use http://(hostip):5000/cpu usage
    2. To get memory percentages over the last 24 hours use http://(hostip):5000/mem usage
    3. To get drive percentages over the last 24 hours use http://(hostip):5000/disk usage
    4. To get current cpu percentages  use http://(hostip):5000/current cpu usage
    5. To get current memory percentages use http://(hostip):5000/current mem usage
    6. To get current drive percentages  use http://(hostip):5000/current disk usage
