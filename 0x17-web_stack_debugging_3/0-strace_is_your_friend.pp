#Code to fix Apache 500 error
exec { 'settingPress':
command  => 'sed -i "s/\b.phpp\b/.php/g" /var/www/html/wp-settings.php',
provider => shell,
}
