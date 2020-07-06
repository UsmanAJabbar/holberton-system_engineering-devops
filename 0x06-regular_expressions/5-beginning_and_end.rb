#!/usr/bin/env ruby
# The goal of this task is to extract "hbtn"
# from the source text, which in this case, is
# being fed by argv/terminal.
# This code extracts words that start with an h
# and end with the char 'n', with at least a
# single character in between the h and n
puts ARGV[0].scan(/h.n/).join
