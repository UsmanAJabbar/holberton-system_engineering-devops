#!/usr/bin/env ruby
# The goal of this task is to extract "hbtn"
# from the source text, which in this case, is
# being fed by argv/terminal.
# This code extracts words that contain htbn,
# regardless of whether or not b exists at
# least once in the text
puts ARGV[0].scan(/hb?tn/).join
