import string
import statistics

# Step 1: Function to generate the histogram (word frequency)
def histogram(source_text):
    # If the input is a filename, open and read the file
    if source_text.endswith('.txt'):
        with open(source_text, 'r') as file:
            source_text = file.read()
    
    # Clean the text, lowercasing it and removing punctuation
    source_text = source_text.lower()
    source_text = source_text.translate(str.maketrans('', '', string.punctuation))
    
    # Split the text into words
    words = source_text.split()
    
    # Create a histogram (word frequency)
    word_freq = {}
    for word in words:
        if word in word_freq:
            word_freq[word] += 1
        else:
            word_freq[word] = 1
            
    return word_freq

# Step 2: Function to get the total count of unique words
def unique_words(histogram):
    return len(histogram)

# Step 3: Function to get the frequency of a specific word
def frequency(word, histogram):
    return histogram.get(word, 0)

# Step 4: Function to find the most frequent word(s)
def most_frequent(histogram):
    max_freq = max(histogram.values())
    most_frequent_words = [word for word, freq in histogram.items() if freq == max_freq]
    return most_frequent_words, max_freq

# Step 5: Function to find the least frequent word(s)
def least_frequent(histogram):
    min_freq = min(histogram.values())
    least_frequent_words = [word for word, freq in histogram.items() if freq == min_freq]
    return least_frequent_words, min_freq

# Step 6: Function to calculate the mean word frequency
def mean_frequency(histogram):
    total_words = sum(histogram.values())
    num_unique_words = len(histogram)
    return total_words / num_unique_words if num_unique_words > 0 else 0

# Step 7: Function to calculate the median word frequency
def median_frequency(histogram):
    frequencies = list(histogram.values())
    return statistics.median(frequencies)

# Step 8: Function to calculate the mode word frequency
def mode_frequency(histogram):
    frequencies = list(histogram.values())
    return statistics.mode(frequencies)
