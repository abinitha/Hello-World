a = []
a.append(["a","b"])
print a
print a[0][1]
print " First "

b = {}
b["karthik"] = "abinitha"
print b
print "second"
b["dumbo"] = ["grk"]
b["dumbo"].append("abinitha")
print b["dumbo"]
print "third"
a = []
for i in range(0,10):
    a.append(i)
print "fourth"
print a

a = {}
a["karthik"] = {}
a["karthik"]["abinitha"] = "dumbo"

print a

a["guldu"] = []
a["guldu"].append({"grk":"guldu"})
a["guldu"].append({"abinitha":"guldu"})

print a
print a["guldu"][0]

z = {}
z["a"] = {}
z["a"]["b"] = []
z["a"]["b"].append("guldu")
print "fifth"
print z
