#!/usr/bin/env ruby
# The goal of this task is to extract "hbtn"
# from the source text, which in this case, is
# being fed by argv/terminal.
# This code finds and returns strings with
# the pattern hbt*n only if t appears between
# 2-5 times in the word
puts ARGV[0].scan(/hbt{2,5}n/).join
