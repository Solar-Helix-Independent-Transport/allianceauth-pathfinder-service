<?php
    ini_set('display_errors', 1);
    ini_set('display_startup_errors', 1);
    error_reporting(E_ALL);
    $api_key=include('api_config.php');
    file_put_contents('./api.log', $api_key."\n", FILE_APPEND);
    file_put_contents('./api.log', $_POST['x-api-key']."\n", FILE_APPEND);
    if ($_POST['x-api-key']==$api_key){
        $file_name="pathfinder-auth.ini";
        $folder="config/";
        $file_name=$folder."".$file_name;
        file_put_contents('./api.log', $_POST['character_ids']."\n", FILE_APPEND);
        file_put_contents('/var/www/html/pathfinder/conf/characters.php', "<?php\nreturn array(".$_POST['character_ids'].");\n?>");
        file_put_contents('./api.log', "CHARACTERS=[".$_POST['character_ids'].']', FILE_APPEND);
        file_put_contents('./api.log', "DONE!"."\n", FILE_APPEND);
        return "Complete";
    }
?>
