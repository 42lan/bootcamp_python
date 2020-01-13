import sys

def text_analyzer(text = None):
	"""
	This function counts the number of upper charactersm lower characters,
	punctuation and spaces in a given text.
	"""
	if (text == None):
		text = str((sys.stdin.readline())).rstrip()
	number_of_characters = len(text);
	number_of_uppercase = sum(1 for c in text if c.isupper());
	number_of_lowercase = sum(1 for c in text if c.islower());
	punctuation_signs = "!\"#$%&'()*+,-./:;<=>?@[\]^_`{|}~";
	number_of_punctuation = sum(1 for c in text if c in punctuation_signs)
	number_of_spaces = sum(1 for c in text if c.isspace());
	print ("The text contains", number_of_characters, "characters:")
	print ("-", number_of_uppercase, "upper letters")
	print ("-", number_of_lowercase, "lower letters")
	print ("-", number_of_punctuation, "punctuation")
	print ("-", number_of_spaces, "spaces")
	return None
