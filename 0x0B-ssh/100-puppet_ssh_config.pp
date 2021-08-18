# set up your client SSH configuration file so that you can connect to a server without typing a password.
exec { 'ssh_config':
  command => 'echo "PasswordAuthentication no" >> /etc/ssh/ssh_config; echo "IdentityFile ~/.ssh/holberton" >> /etc/ssh/ssh_config',
  path    => '/bin',
}
