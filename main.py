def main ():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
        print(file_contents)
        return file_contents

def word_count():

    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
        words = file_contents.split()
        wordcount = len(words)
        print (f"{wordcount} words were found in the document")
    return wordcount

def character_dictionary():

    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
        full_lower_case = file_contents.lower()
        character_dict = {}
        for i in full_lower_case:
            if i in character_dict:
                character_dict[i] += 1
            else:
                character_dict[i] = 1
        
        character_list = []
        for item in character_dict:
            if item.isalpha():

                count = character_dict[item] 
                character_list.append({"char": item, "num": count})
        
        character_list.sort(key=lambda x: x["num"], reverse=True)

        for char in character_list:
            print (f"The '{char['char']}' character was found '{char ['num']}' times")
        return character_list


        

#main()
word_count()
character_dictionary()

