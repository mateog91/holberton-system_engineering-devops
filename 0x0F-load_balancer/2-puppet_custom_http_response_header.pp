# Just as in task #0, we’d like you to automate the task of creating a custom HTTP header response, but with Puppet.

#     The name of the custom HTTP header must be X-Served-By
#     The value of the custom HTTP header must be the hostname of the server Nginx is running on
#     Write 2-puppet_custom_http_response_header.pp so that it configures a brand new Ubuntu machine to the requirements asked in this task

package { 'nginx install':
    provider    => 'nginx'
    
}

file_line { '/etc/nginx/sites-available/default':
    ensure => present,
    line => "add_header X-Served-By $HOSTNAME"
}

exec { 'service':
  path     => '/usr/bin:/usr/sbin:/bin',
  command  => 'sudo service nginx restart',
  provider => shell,
}
