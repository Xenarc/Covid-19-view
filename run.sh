#!/bin/bash
cd /var/www/html/Covid
rm -f -R -d ./COVID-19
git clone https://github.com/CSSEGISandData/COVID-19.git
python ./covid.py

echo "Done"
