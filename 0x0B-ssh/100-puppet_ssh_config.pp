#!/usr/bin/env bash
# edit configuration automatically, across multiple systems

file_line { 'Turn off passwd':
  ensure  => present,
  path    => '/etc/ssh/ssh_config',
  line    => '     PasswordAuthentication no',
  replace => true,
}

file_line { 'identity change':
  ensure  => present,
  path    => '/etc/ssh/ssh_config',
  line    => '     IdentityFile ~/.ssh/school',
  replace => true,
}
