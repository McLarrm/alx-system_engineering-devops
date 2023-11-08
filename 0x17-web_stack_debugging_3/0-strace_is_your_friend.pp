# Typo in wp-settings.php
exec { 'fix php extension typo':
  command => '/bin/sed -i "s/.phpp/.php/g" /var/www/html/wp-settings.php',
}
