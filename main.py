import sys

alphabet = "abcdefghijklmnopqrstuvwxyz"

print("====This Message Is Encrypted====")

while True:
    print("\nmenu")
    print("1.Encrypted (encrypt message)")
    print("2.Encrypted (encrypt password)")
    print("3.Exit")


    choose = input("Choose (1/2/3): ").strip()

    if choose == "3":
        print("the application will be closed, goodbye")
        break  

    if choose not in ["1", "2"]:
        print("Invalid choice! Please select 1, 2, or 3.")
        continue 
        
    real_message = input("Enter Message: ")

    shift = 3 if choose == "1" else -3
    result_message = ""

    for huruf in real_message:
        if huruf.isalpha():
            capital = huruf.isupper()
            small = huruf.lower()

            old_index = alphabet.index(small)
            new_index = (old_index + shift) % 26
            new_letter = alphabet[new_index]
            
            result_message += new_letter.upper() if capital else new_letter
        else:
            result_message += huruf

    result = "your secret message" if choose == "1" else "Real you message"
    print(f"{result}: {result_message}")
