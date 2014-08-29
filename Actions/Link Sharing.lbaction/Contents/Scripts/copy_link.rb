#!/usr/bin/ruby

require 'json'

url = JSON.parse(ARGV[0])

items = []
url.each do |value|
    #puts value.values
    items.push(value.values.to_s)
end

def copy_to_clipboard(value)
    `echo "#{value}" |pbcopy`
    return 0
end

report = ''
i = 0
itemsLength = items.length
while i < itemsLength
    report << "#{items[i]}\n"
    i += 1
end

report.gsub!(/\[/, '')
report.gsub!(/\]/, '')
copy_to_clipboard(report)
