#!/usr/bin/env ruby
# The goal of this task is to extract "hbtn"
# from the source text, which in this case, is
# being fed by argv/terminal.
# This code extracts words that contain htbn,
# with the character 't' appearing at least
# once and an infinite number thereafter
puts ARGV[0].scan(/hbt+n/).join
