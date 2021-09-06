a = ["fb.com", "tw.com", "cat.com"]

for i in a:
    if "fb" in i:
        pass
    if "tw" in i:
        pass
    else:
        print(i)

print("\n\n")

for i in a:
    if "fb" in i:
        pass
    elif "tw" in i:
        pass
    else:
        print(i)
