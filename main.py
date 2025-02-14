
def main():
    full_text = get_text()
    num_words = word_count()
    num_chars = char_count(full_text)
    report_title, report_words, report_list, report_footer = create_report(num_chars, num_words)
    print(report_title)
    print(report_words)
    print("")
    for item in report_list:
        print(f"The '{item[0]}' character was found {item[1]} times")

    print(report_footer)

def get_text():
    with open("books/frankenstein.txt") as f:
        return f.read()

def word_count():
    with open("books/frankenstein.txt") as w:
        words = w.read().split()
    return len(words)

def char_count(text):
    chars = {}
    for c in text:
        c_low = c.lower()
        if c_low in chars:
            chars[c_low] += 1
        else:
            chars[c_low] = 1
    return chars

def find_key(item):
    return item[1]

def create_report(char_dict, words):
    title = "--- Begin report of books/frankenstein.txt ---"
    chars = f"{words} words found in the document"
    alpha_dict = {}
    sorted_char_list = []
    footer = "--- End report ---"
    

    for item in char_dict:
        if item.isalpha():
            alpha_dict[item] = char_dict[item]

    sorted_char_list = sorted(alpha_dict.items(), key=find_key, reverse=True)

    return title, chars, sorted_char_list, footer
main()