setpoint = 100
current_value = 85
kp = 0.5

error = setpoint - current_value
output = kp * error

print(f"Error: {error}")
print(f"Control Output: {output}")