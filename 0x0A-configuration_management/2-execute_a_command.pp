# Creating a manifest that kills a process
# called killmenow

exec { 'pkill':
  command => '/usr/bin/pkill  killmenow',
  provider => 'shell',
}
