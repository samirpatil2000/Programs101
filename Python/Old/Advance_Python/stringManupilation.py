import textwrap

# value = """This function wraps the input paragraph such that each line
# in the paragraph is at most width characters long. The wrap method
# returns a list of output lines. The returned list
# is empty if the wrapped
# output has no content."""
value='<RequestsCookieJar[<Cookie csrftoken=NM4GmBIW0jxoPdxeSLZ0Puko6HwXvJNsdSfYUKdD84PzMMpqqvi7D2iKXBE7Kb6m for curiosityishere.pythonanywhere.com/>]>'

# Wrap this text.
wrapper = textwrap.TextWrapper(width=80)

word_list = wrapper.wrap(text=value)

# Print each line.
for element in word_list:
	print(element)

# print(len(tex))

