target = 100
current = 80

error = target - current

kp = 0.5
ki = 0.1
kd = 0.1

output = kp * error

print(output)
