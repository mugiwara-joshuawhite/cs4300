def count_words_in_file(filepath: str) -> int:
    '''
    count_words_in_file
    Opens a file and returns number of words in that file
    '''
    try:
        fl = open(filepath)
    except FileNotFoundError:
        print("Critical error: File not found. Check the filepath")
        return 0
    
    return len(fl.read().split())