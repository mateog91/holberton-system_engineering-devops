# Sky is the limit, let's bring that limit higher
# Config file for debugging task
exec { 'fix--for-nginx':
  command => 'sed -i "s/15/4096/" /etc/default/nginx',
  path    => '/usr/local/bin/:/bin/'
}
# Restart Nginx
exec { 'Restart_Nginx':
  command => 'nginx restart',
  path    => '/etc/init.d/'
}
