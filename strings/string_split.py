# Purpose:  Demonstrating splitting strings cleanly in Python 2

test_string = "This is a test string"

if __name__ == "__main__":
    print "The string we are starting with is:"
    print test_string
    print "We can remove the first letter and keep rest with [1:]"
    print test_string[1:]
    print "We can remove the last letter and keep rest with [:-1]"
    print test_string[:-1]
    print "We can split the string into a list of smaller strings with the split command, define delimiter as \" \""
    print test_string.split(" ")
    print "We can change what delimiter we use. Now using \"e\""
    print test_string.split("e")