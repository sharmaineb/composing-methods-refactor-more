# by Kami Bigdely
# Rename Method
# Reference: https://parade.com/1039985/marynliles/pick-up-lines/

def calculate_area_under_graph(graph):
    """calculate the area under the input graph."""
    pass

def find_maximum_value(list_values):
    """find and return the maximum value in the list."""
    max_value = list_values[0]
    for value in list_values:
        if value > max_value:
            max_value = value
    return max_value

li = [5, -1, 43, 32, 87, -100]
print(find_maximum_value(li))

def split_sentence_into_words(sentence):
    """split the input sentence into a list of words and return it."""
    words = sentence.split(' ')
    return words

print(split_sentence_into_words('If you were a vegetable, you’d be a ‘cute-cumber.'))