def initial(filename):
    with open(filename, "w+") as b:
        b.read()
        if b.tell() == 0:
            b.write("Day 1: Started my secret diary.")

def main_handling(file):
    initial(file)
    
    with open(file, "a") as b:
        b.write("\n\nDay 2: Learned about file handling in Python.")
    
    with open(file, "r") as b:
        for n in range(3):
            num = int(input("Enter the num |1,2,3| => "))
            if num == 1:
                b.seek(0)
                print(b.read())
            elif num == 2:
                b.read()
                print("Pointer currently at", b.tell())
                b.seek(0)
                print("Pointer reset to", b.tell())
                print(b.readline())
            else:
                b.seek(0)
                print(b.readlines())
    
    with open(file, "r+") as b:
        old = b.read()
        b.seek(0)
        b.write("*** Confidential Diary ***\n" + old)
    
    searching(file)
    return "Diary handling complete!"

def searching(file):
    with open(file, "r") as b:
        content = b.read()
        
        if "Python" in content:
            print("Word found!")
        else:
            print("Word not found!")
            
        index = content.find("Python")
        print("Index at which 'Python' was found:", index)
        
        counts = content.count("Diary")
        print("Occurrences of 'Diary':", counts)
        
        b.seek(0)
        for i, line in enumerate(b, start=1):
            if "Diary" in line:
                print(f"Found 'Diary' in line {i}: {line.strip()}")

result = main_handling("diary.txt")
print(result)
