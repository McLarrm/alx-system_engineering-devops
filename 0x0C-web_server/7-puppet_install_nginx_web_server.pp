# Install Nginx package
package { 'nginx':
  ensure => 'installed',
}

# Ensure Nginx is running and enabled
service { 'nginx':
  ensure  => 'running',
  enable  => true,
  require => Package['nginx'],
}

# Create a custom HTML page with "Hello World!"
file { '/var/www/html/index.html':
  ensure  => 'file',
  content => 'Hello World!',
  require => Package['nginx'],
}

# Nginx configuration file for the root path
file { '/etc/nginx/sites-available/default':
  ensure  => 'file',
  content => template('nginx/default.erb'),
  require => Package['nginx'],
  notify  => Service['nginx'],
}

file { '/etc/nginx/sites-enabled/default':
  ensure => 'link',
  target => '/etc/nginx/sites-available/default',
  require => File['/etc/nginx/sites-available/default'],
  notify => Service['nginx'],
}

file { '/etc/nginx/sites-available/redirect_me':
  ensure  => 'file',
  content => template('nginx/redirect_me.erb'),
  require => Package['nginx'],
  notify  => Service['nginx'],
}

file { '/etc/nginx/sites-enabled/redirect_me':
  ensure => 'link',
  target => '/etc/nginx/sites-available/redirect_me',
  require => File['/etc/nginx/sites-available/redirect_me'],
  notify => Service['nginx'],
}
