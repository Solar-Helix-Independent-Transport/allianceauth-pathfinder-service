#!/bin/bash
function replace_setting() {
    sed -i -E "s/$1/$2/g" $3
}
echo "Replacing settings!"
replace_setting "CHARACTER\s*=\s*.*" "CHARACTER          =   $1" "/var/www/pathfinder/app/pathfinder.ini"
echo "Complete!"
