#!/usr/bin/env ruby
# The goal of this task is to extract "hbtn"
# from the source text, which in this case, is
# being fed by argv/terminal.
# This code extracts and returns all the
# captial letters found in the given text
puts ARGV[0].scan(/[A-Z]/).join
