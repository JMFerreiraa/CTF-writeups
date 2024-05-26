from pwn import *

tickets = ((1, 2, 3, 4, 5, 6 ),(1, 2, 3, 4, 7, 8 ),(1, 2, 5, 6, 7, 8 ),
        (60, 61, 62, 63, 64, 65), (60, 66, 67, 68, 69, 70), (61, 66, 62, 67, 63, 69), (1, 2, 3, 60, 61, 62), (1, 2, 3, 63, 64, 65), (1, 2, 3, 66, 67, 68) ,(1, 2, 3, 4, 69, 70), (4, 5, 6, 60, 62, 64), (4,5,6, 66,68,70), (4, 5, 6, 61, 63, 65), (4, 5, 6, 67, 69, 70), (7,8, 9, 60, 65, 70), (7, 8, 9, 61, 69, 70), (7, 8, 9, 65, 67, 68), (7,8, 62, 63, 64, 67), (7, 8, 9, 63, 70, 66), (63,64,65,66,67,68), (60,61,62,68,69,70), (63,64,65,68,69,70),
        (9, 10, 11, 12, 13, 14),(9, 10, 11, 15, 16, 17),(12, 13, 14, 15, 16, 17),
        (18, 19, 20, 21, 26, 27),(18, 19, 22, 23, 30, 31),(18, 19, 24, 25, 28, 29),(20, 21, 22, 23, 28, 29),(20, 21, 24, 25, 30, 31),(22, 23, 24, 25, 26, 27),(26, 27, 28, 29, 30, 31),
        (32, 33, 34, 35, 40, 41),(32, 33, 36, 37, 44, 45),(32, 33, 38, 39, 42, 43),(34, 35, 36, 37, 42, 43),(34, 35, 38, 39, 44, 45),(36, 37, 38, 39, 40, 41),(40, 41, 42, 43, 44, 45),
        (46, 47, 48, 49, 54, 55),(46, 47, 50, 51, 58, 59),(46, 47, 52, 53, 56, 57),(48, 49, 50, 51, 56, 57),(48, 49, 52, 53, 58, 59),(50, 51, 52, 53, 54, 55),(54, 55, 56, 57, 58, 59))
    
  

print(len(tickets))

# Establish a connection
conn = remote('challenge.nahamcon.com', 30392)

# Your code here
initial_text = conn.recvuntil(">> ")
print(initial_text)
conn.sendline(str(len(tickets)))


#NOTE: I did not save my solution for this one and the challenges are down at the moment, so this code is untested but the tickets on top are correct and working.
for ticket in tickets:
    for value in ticket:
        input_start = conn.recvuntil(">> ")
        conn.sendline(str(value))


conn.interactive()

# Close the connection
conn.close()