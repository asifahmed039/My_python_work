line='my name is sunny.'
key='nam0'
for x in line:
    if key.lower() in line.lower():
        print(key.strip())
        break