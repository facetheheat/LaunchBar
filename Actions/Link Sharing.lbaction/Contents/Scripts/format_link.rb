#!/usr/bin/ruby

require 'json'

url = ARGV[0]

case url
  when /^(smb:\/\/)/
    a1 = url.clone.gsub(/^(([^:\/??#]+?):)??(\/\/)/imx, "\\\\\\\\\\")
    a2 = a1.gsub!("\/", "\\")
    b1 = url.clone.gsub("smb", "afp")
    c1 = url.clone.gsub("smb", "cifs")
    printList = [a2, b1, c1, url]

  when /^(cifs:)/
    a2 = url.clone.gsub(/^(([^:\/??#]+?):)??(\/\/)/imx, "\\\\\\\\\\")
    a3 = a2.gsub!("\/", "\\")
    b1 = url.clone.gsub("cifs", "afp")
    c1 = url.clone.gsub("cifs", "cifs")
    printList = [a3, b1, c1, url]

  when /^(\/\/)/
    a1 = url.clone.gsub(/^(([^:\/??#]+?):)??(\/\/)/imx, "\\\\\\\\\\")
    a2 = a1.gsub!("\/", "\\")
    b1 = url.clone.gsub("//", "afp://")
    c1 = url.clone.gsub("//", "smb://")
    d1 = url.clone.gsub("//", "cifs://")
    printList = [a2, b1, c1, d1, url]

  when /^(\\)/
    a1 = url.clone.gsub(/^(([\\+\\]))/imx, "//")
    a2 = a1.gsub!("\\", "/")
    a3 = a2.gsub!("///", "//")
    b1 = a3.clone.gsub("//", "afp://")
    c1 = a3.clone.gsub("//", "smb://")
    d1 = a3.clone.gsub("//", "cifs://")
    printList = [a3, b1, c1, d1, url]

  when /^(afp:)/
    a2 = url.clone.gsub(/^(([^:\/??#]+?):)??(\/\/)/imx, "\\+\\")
    a3 = a2.gsub!("\/", "\\")
    b1 = url.clone.gsub("afp", "smb")
    c1 = url.clone.gsub("afp", "cifs")
    printList = [a3, b1, c1, url]
  else
    puts "Unknown URL\n"
    exit 0
end

items = []

item = {}
item['title'] = 'Copy All'
item['icon'] = 'Share Link.png'
item['action'] = 'copy_link.rb'

argumentList = []
printList.each do |selectedValue|
    outputArgument = {}
    outputArgument[selectedValue] = selectedValue
    argumentList.push(outputArgument)
end
item['actionArgument'] = argumentList.to_json

items.push(item)

printList.each do | value |
    item = {}
    item['title'] = value
    item['icon'] = 'Document.png'
    item['action'] = 'copy_link.rb'
    argumentOutput = []
    actionOutput = {}
    actionOutput[value] = value
    argumentOutput.push(actionOutput)
    item['actionArgument'] = argumentOutput.to_json
    items.push(item)
end

puts items.to_json
