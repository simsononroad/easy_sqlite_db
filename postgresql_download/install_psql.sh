#!/bin/bash

set -e



sudo apt-get update
sudo apt-get install postgresql postgresql-contrib
sudo su postgres
echo "You can add user: 'ALTER CREATE USER [username] WITH PASSWORD '[password]'; '"
echo "You can change password: 'ALTER USER [username] WITH PASSWORD '[password]'; '"
echo "You can add permission: 'ALTER USER [username] WITH [rang]; '"
echo "Wirte 'psql' to terminal to run this commands"