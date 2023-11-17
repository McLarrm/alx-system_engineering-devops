# Fix user limits.conf
exec { 'fix limits.conf':
  path    => ['/usr/bin', '/sbin', '/bin', '/usr/sbin'],
  command => 'sed -i "s/nofile 5/nofile 4000/g" /etc/security/limits.conf; sed -i "s/nofile 4/nofile 4000/g" /etc/security/limits.conf',
}
