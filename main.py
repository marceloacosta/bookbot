def main():
    
    def read_text(file_path):
        with open(file_path) as f:
            file_contents = f.read()
        return file_contents
    
    def count_words(text):
        return len(text.split())

    def create_dict():
        counter = {}
        for character in  "abcdefghijklmnopqrstuvwxyz1234567890 ',()\n.-_:;[]¨{}#$%&//=?¿|*!":
            counter[character] = 0
        return counter


    def count_characters(text):
        text_lower = text.lower()
        counter = create_dict()
        for character in text_lower:
            if character in counter:
                counter[character] += 1
            
        return counter




    path = "books/frankenstein.txt"
    total_chars = count_words(read_text(path))

    print(f" --- Begin report of {path} ---")
    print(f"{total_chars} words found in the document \n")
    character_count = count_characters(read_text(path))

    for key,value in character_count.items():
        print(f"The {key} character was found {value} times")










main()