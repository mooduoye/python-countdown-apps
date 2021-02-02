import time

def countdown(n):
    "countdown() funtion with postional 'n' parameter"
    for i in range(n):
        print(n - i)
        time.sleep(1)
     
# Call countdown funtion with positiona arguments '5'   
countdown(5)
output_message = 'WELCOME'

print(output_message)

    