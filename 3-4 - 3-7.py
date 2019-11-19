guest_list = ["vincentius", "arnold", "ohyeah"]
print(guest_list)
for i in range(3):
    print("Dear" + " " + guest_list[i] + " " + "You have been invited to dinner")
del guest_list[2]
guest_list.insert(2,"ouhnouh")
print(guest_list)
for i in range(3):
    print("Dear" + " " + guest_list[i] + " " + "You have been invited to dinner")
for i in range(3):
    print("Dear" + " " + guest_list[i] + " " + "we have found a bigger table")
guest_list.insert(0,"timotius")
guest_list.insert(2,"piliph")
guest_list.append("ohoh")
for i in range(6):
    print("Dear" + " " + guest_list[i] + " " + "You are invited to dinner")

print(guest_list.pop() + " " + "you don't desesrve to come")
print(guest_list.pop() + " " + "you don't desesrve to come")
print(guest_list.pop() + " " + "you don't desesrve to come")
print(guest_list.pop() + " " + "you don't desesrve to come")

for i in range(2):
    print("Dear" + " " + guest_list[i] + " " + "You are still invited to dinner")
