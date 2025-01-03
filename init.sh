#!/bin/bash

set -e

echo "Installing easy_db Python library"
git clone https://github.com/simsononroad/easy_sqlite_db.git
cd easy_sqlite_db
mv easy_db ../
cd ..
sudo rm -r easy_sqlite_db
cat > main.py << EOF
from easy_db import *
EOF
