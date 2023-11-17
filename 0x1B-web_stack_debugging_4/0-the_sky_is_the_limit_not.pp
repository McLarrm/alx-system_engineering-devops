# Expand nginx user limit
exec { 'expand nginx user limit and restart webserver':
  path    => ['/usr/bin', '/sbin', '/bin', '/usr/sbin'],
  command => 'sed -i "s/15/4000/g" /etc/default/nginx; service nginx restart',
}
