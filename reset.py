import re, mechanize
br = mechanize.Browser()
br.add_password("http://192.168.252.71", "admin", "22222")
br.open("http://192.168.252.71/reset.html")
br.select_form(nr=0)
c=br.form.controls[3]
c.readonly=False
br.form["resetOption"]="1"
response=br.submit()
print response.read()
br.open("http://192.168.252.71/reset.html")
br.select_form(nr=0)
c=br.form.controls[3]
c.readonly=False
br.form["resetOption"]="0"
response=br.submit()
print response.read()