#!/usr/bin/env ruby
# The goal of this task is to extract "hbtn"
# from the source text, which in this case, is
# being fed by argv/terminal.
# This code handles and finds hbtn regardless of
# how many 't' characters are present in the text
puts ARGV[0].scan(/hbt*n/).join
