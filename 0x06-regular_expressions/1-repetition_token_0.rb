#!/usr/bin/env ruby
puts ARGV[0].scan(/^[a-z]{2}[a-z]{2,5}[a-z]{1}$/).join
