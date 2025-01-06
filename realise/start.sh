#!/bin/bash

set -e

echo "Letöltés: easy_db Python library"
git clone https://github.com/simsononroad/easy_sqlite_db.git
cd easy_sqlite_db
mv easy_db ../
cd ..
echo "Az esetleg felbukkanó jelszó kérés a felesleges mappa törléséhez szükséges!"
sudo rm -r easy_sqlite_db
cat > yourfile.py << EOF
from easy_db import *
def main():
    pass
if __name__ == "__main__":
    main()
EOF

echo "Késsz"
echo "Verzió: 1.1"