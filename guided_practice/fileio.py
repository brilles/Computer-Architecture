import sys #in unix land 0 exit == success, non-zero means it fail in some way -- echo $? to check after program are run

if len(sys.argv) != 2:
    print(f"usage: {sys.argv[0]} filename")
    sys.exit(1)

try:
    with open(sys.argv[1]) as f:
        for line in f:
            num = line.split('#', 1)[0]
            
            if num.strip() == '':
                continue
  
            memory[address] = int(num)
            address += 1

except FileNotFoundError:
    print(f"{sys.argv[0]}: {sys.argv[1]} not found")
    sys.exit(2)