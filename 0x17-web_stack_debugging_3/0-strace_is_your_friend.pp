# Apache return 500 solved with puppet

exec { 'apache2_500':
  command => "/bin/sed -i 's/.phpp/.php/g' /var/www/html/wp-settings.php",
}
