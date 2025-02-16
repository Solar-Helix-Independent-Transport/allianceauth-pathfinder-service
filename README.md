# Pathfinder service

This very simply creates a whitelist of EVERY character or alt of main that enables the service. As this list can be HUGE, i had to edit pathfidner a little bit as the config files were not loadable by php.


## Installation

TLDR 
- add 2 new files to the PF install
  - pathfinder/api_config.php
  - pathfinder/api_write.php
- Overide 1 file
  - pathfinder/app/Model/Pathfinder/CharacterModel.php
- Add a new folder to catch the state changes between reboots of PF
  - pathfinder/conf


**WIP instructions - Use at your own peril, orr be good at debugging and update them for me!**

1. `pip install git+url.of.repo` or add to your req.txt for docker installs
1. add `PATHFINDER_API_KEY="SomeREallyGoodAPIPassword123.SrslyMakeitGood!"`
1. migrate and restart auth etc.
1. copy the following files into your pathfinder install location ( i am using docker compose - YMMV  )
   - `wget https://raw.githubusercontent.com/Solar-Helix-Independent-Transport/allianceauth-pathfinder-service/refs/heads/main/api_config.php`
   - Update the password in this file to match your `PATHFINDER_API_KEY` really good key you randomly generated. DO NOT use the default above...
   - `wget https://raw.githubusercontent.com/Solar-Helix-Independent-Transport/allianceauth-pathfinder-service/refs/heads/main/api_write.php`
   - pull down the modified `CharacterModel` file `wget https://raw.githubusercontent.com/Solar-Helix-Independent-Transport/allianceauth-pathfinder-service/refs/heads/main/CharacterModel.php`
   - add the following volumes to your pathfinder service in docker compose
    ```yaml
    pf:
        hostname: pathfinder
        image: ghcr.io/goryn-clade/pathfinder:latest
    .....
        volumes:
    .....
        - ./pathfinder/config/pathfinder/conf:/var/www/html/pathfinder/conf
        - ./pathfinder/overrides/CharacterModel.php:/var/www/html/pathfinder/app/Model/Pathfinder/CharacterModel.php
        - ./pathfinder/api_write.php:/var/www/html/pathfinder/api_write.php
        - ./pathfinder/api_config.php:/var/www/html/pathfinder/api_config.php
    .....
    ```
   - ensure the first half of the paths is accurate ( in this example `./pathfinder/api_write.php` because all my pathfinder configs are organised in a folder called pathfinder ) do not change the container mount path `:var/www...etc` these are critical.
1. do what ever else needs doing...