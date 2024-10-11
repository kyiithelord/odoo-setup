odoo configure
* init postgresql
sudo service postgresql status
sudo su postgres
psql
CREATE USER odoo;
ALTER USER odoo SUPERUSER;
ALTER ROLE odoo WITH LOGIN;
ALTER USER odoo WITH ENCRYPTED PASSWORD 'odoo';
cd /etc/postgresql
sudo service postgresql restart

*to fix with at nano
sudo nano pg_hba.conf
(local    odoo    all    trust)

*to init myenv-file
python3 -m pip install setuptools wheel
python3 -m pip install -r requirements.txt

* run database server
./odoo-bin --xmlrpc-port=8071 --addons-path=./addons --db_user=odoo --db_password=odoo


* run project
./odoo-bin --xmlrpc-port=8071 --addons-path=./addons,custom_addons --db_user=odoo --db_password=odoo

* 
