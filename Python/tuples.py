# We write tuples in parentheses instead of square brackets.
# fullname = ('Grace', 'M', 'Harper')
# print(fullname)



def file_size(file_info):
    print(file_info)
    name, type, size = file_info
	return("{:.2f}".format(size / 1024))

print(file_size(('Class Assignment', 'docx', 17875))) # Should print 17.46
print(file_size(('Notes', 'txt', 496))) # Should print 0.48
print(file_size(('Program', 'py', 1239))) # Should print 1.21
