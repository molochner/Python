# input a string.. output morse code

# letters and numbers.. 62 total
letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 
           'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 
           'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z',
           '1','2','3','4','5','6','7','8', '9','0',
           'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 
           'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 
           's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
 
codes = [".-","-...","-.-.","-..",".","..-","--.","....",
            "..",".---","-.-",".-..","--","-.","---",".--.",
            "--.-",".-.","...","-","..-","...-",".--","-..-",
            "-.--","--..",".----","..---","...--","....-",
            ".....","-....","--...","---..","----.","-----",
            ".-","-...","-.-.","-..",".","..-","--.","....",
            "..",".---","-.-",".-..","--","-.","---",".--.",
            "--.-",".-.","...","-","..-","...-",".--","-..-",
            "-.--","--.."]

def string_to_morse(mess_str):
    morse_message = ''
    str_length = len(mess_str)
    i = 0
    while i < str_length:
        j = 0
        while j < 62:
            if mess_str[i] == letters[j]:
                morse_message += codes[j]
                morse_message += ' '
            elif mess_str[i] == ' ':
                morse_message += '_'
            j += 1
        i += 1
    return morse_message

message = input("Enter a message to display in morse code: ")
message = str(message)

print(string_to_morse(message))