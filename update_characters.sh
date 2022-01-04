#!/bin/bash
echo $1
function replace_setting() {
    mkdir /var/www/html/pathfinder/conf/
    sed -E "s/$1/$2/g" $3 > /var/www/html/pathfinder/conf/pathfinder.ini;
}
echo "Replacing settings!"
replace_setting "CHARACTER\s*=\s*.*" "CHARACTER                     =   $1" "/var/www/html/pathfinder/app/pathfinder.ini"
echo "Complete!"
