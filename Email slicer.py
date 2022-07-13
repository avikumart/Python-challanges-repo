# Email slicer
email = input("Enter your email ID: ")
stripped = email.strip()
name = stripped[:stripped.index('@')]
domain_name = stripped[stripped.index('@')+1:]
print(name)
print(domain_name)

words = "we are the ones who learn on the go".split()
joined = "-".join([word.upper() for word in words])
print(joined)
