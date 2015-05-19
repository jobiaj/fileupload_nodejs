#ve out bad and just compare against
# x at the end if memory is more important than speedi
x = [1,2,3,4,4,5,6,7,7]
y = [3,4,5,6,7,8,9,10]
newx, bad, newy = [], [], []
for i in x:
    if i in y:
      #  callsomefunction(i)
        bad.append(i)
    else:
        newx.append(i)

for i in y:
    if i not in bad:
        newy.append(i)

print newx
print newy
