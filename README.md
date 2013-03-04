#Require:
- Django==1.4.5
- MySQL-python

#Installation:
Recommended installation on [virtualenv](http://www.virtualenv.org/)

    % mkdir -p ~/venv && cd ~/venv
    % virtualenv --no-site-packages --use-distribute ./astctl && cd ./astctl
    % source bin/activate
    % pip install django==1.4.5
    % pip install MySQL-python

    % mkdir -p ./projects && cd ./projects
    % git clone git://github.com/iddqd3/asterctl.git && cd ./asterctl

Rename `mysql.cnf-example` to `mysql-cnf` and edit
Rename `asterctl/settings.py-example` to `asterctl/settings.py` and edit follow variables:
- ADMINS
- CDR_DB
- PEER_DB
- TIME_ZONE

    % ./manager.py syncdb
    % ./manager.py runserver [ip:port]
