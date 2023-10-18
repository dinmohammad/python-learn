employee_fle =  open("read_file.txt", 'a')

# for employee in employee_fle.readlines():
#     print(employee)

employee_fle.write("\n ASH - Ashikur Rahaman")
employee_fle.close()

employee_html = open("write_file.html", "w")
employee_html.write("<p>This is HTML</p>")
employee_html.close()