def encode_rot(text, key):
    """
    Encodes a string using the ROT algorithm. 
    Logic: Uses modulo 26 arithmetic to shift alphabet letters while 
    preserving case and ignoring non-alphabetic characters.
    """
    result = ""
    for char in text:
        if char.isalpha():
            start = ord('A') if char.isupper() else ord('a')
            # The modulo operator (%) ensures the shift wraps around the 26 letters
            new_pos = (ord(char) - start + key) % 26
            result += chr(start + new_pos)
        else:
            result += char
    return result

def decode_rot(ciphertext):
    """
    Decodes a message by testing all 26 possible keys.
    Logic: Compares each trial decryption against 'Dictionary.txt'. 
    The version with the most dictionary matches is printed as the result.
    """
    try:
        with open("dictionary.txt", "r") as f:
            dictionary = {word.strip().lower() for word in f}
    except FileNotFoundError:
        print("Error: Dictionary.txt not found. Ensure it is in the same directory.")
        return

    best_key = 0
    max_matches = -1
    best_text = ""

    for key in range(26):
        # We use a negative key to reverse the rotation
        trial_text = encode_rot(ciphertext, -key)
        
        # Split text into words and remove punctuation for checking
        words = trial_text.split()
        match_count = sum(1 for w in words if "".join(filter(str.isalpha, w)).lower() in dictionary)
        
        if match_count > max_matches:
            max_matches = match_count
            best_key = key
            best_text = trial_text
            
    print(f"The clear text is : \"{best_text}\"")
    print(f"The key is {best_key}")

# ==========================================
# TEST CASES
# ==========================================

# --- Part A: Required Test ---
print("--- Part A: Encoding Test ---")
clear_text_a = " Machine CAN learn 2 !!!"
print(f"Input: {clear_text_a}")
print(f"Output: {encode_rot(clear_text_a, 28)}")
print("-" * 30)

# --- Part B: Required Test ---
print("\n--- Part B: Decoding Test ---")
cipher_text_b = "Tqjq yi byau fuefbu, ydjuhhewqju yj xqht udekwx qdt yj mybb jubb oek mxqjuluh oek mqdj je xuqh."
decode_rot(cipher_text_b)
print("-" * 30)

# --- Part C: Additional Ciphertext Tests ---
print("\n--- Part C: Additional Ciphertext Tests ---")

# Custom Message Test using your name
custom_message = "Hi everyone My name is Pardha Saradhi Edupalli"
# Using a key of 15 for the rotation
encoded_custom = encode_rot(custom_message, 15)

print(f"Testing Custom Ciphertext: {encoded_custom}")
decode_rot(encoded_custom)

print()

# Second test case (Key of 7)
test_2 = encode_rot("Python is useful for cybersecurity automation.", 7)
print(f"Testing Ciphertext 2: {test_2}")
decode_rot(test_2)

# This notebook implements a ROT (Rotation) cipher encoder and an automated decoder. The encode_rot function shifts alphabet letters while ignoring symbols and numbers. The decode_rot function is a "smart" decoder; it tests all 26 possible shift keys and compares the results against a dictionary file (Dictionary.txt). The key that produces the highest number of recognized English words is identified as the correct key.
