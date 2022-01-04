<?php
error_reporting(E_ALL);
    $api_key=include('api_config.php');
    if ($_POST['x-api-key']==$api_key){
        $file_name="pathfinder-auth.ini";
        $folder="config/";
        $file_name=$folder."".$file_name;
        $output = shell_exec('/var/www/html/pathfinder/app/update_characters.sh '.$_POST['character_ids']);
        return $output
    }
/>

