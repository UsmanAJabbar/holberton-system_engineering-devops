#!/usr/bin/env ruby
# The goal of this task is to extract "hbtn"
# from the source text, which in this case, is
# being fed by argv/terminal.
# This code extracts words that contain htbn,
# with the character 't' appearing an unlimited
# number of times or not at all
puts ARGV[0].scan(/hbt*n/).join
