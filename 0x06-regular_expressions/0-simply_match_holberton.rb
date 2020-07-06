#!/usr/bin/env ruby
# The goal of this task is to extract "Holberton"
# from the source text, which in this case, is
# being fed by argv/terminal.
puts ARGV[0].scan(/Holberton/).join
