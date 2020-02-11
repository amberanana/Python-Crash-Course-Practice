# 3-4
guest_list = ["Madoka", "Homura", "QB"]
print(guest_list)

# 3-5
print(guest_list[2] + " can't come to dinner.")
guest_list = ["Madoka", "Homura", "Sayaka"]
print(guest_list)

# 3-6
guest_list.insert(0, 'Mami')
guest_list.insert(1, 'Tatsuya')
guest_list.append('Kyoko')
print(guest_list)

# 3-7
adios_1 = guest_list.pop()
print("Sorry " + adios_1.title() + ", you can't come to the dinner.")
adios_2= guest_list.pop()
print("Sorry " + adios_2.title() + ", you can't come to the dinner.")
adios_3= guest_list.pop()
print("Sorry " + adios_3.title() + ", you can't come to the dinner.")
adios_4= guest_list.pop()
print("Sorry " + adios_4.title() + ", you can't come to the dinner.")

print(guest_list[0] + ", welcome to my dinner party!")
print(guest_list[1] + ", welcome to my dinner party!")

del guest_list

