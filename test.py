
#
a = 45670
# a = 7863121
# a = 7863121
# ../dist/configure --disable-shared --enable-cxx --with-pic --prefix=BDB_PREFIX
# Input: 01
# Output: 1 0
#
# Input: 45670
# Output: 12 10
#
# Input: 7863121
# Output: 12 16
#
# Input: 77620
# Output: 14 8
#
# Input: 1357
# Output: 16 0
#
# Input: 240664826606
# Output: 0 50
count = len(str(a))

total = sum([int(item) for item in str(a)])

print(total, count)
print(total/count)



