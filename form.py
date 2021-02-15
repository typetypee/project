import cgi, cgitb
formData = cgi.FieldStorage();
name_input = formData.getValue('name_input');
print(name_input);