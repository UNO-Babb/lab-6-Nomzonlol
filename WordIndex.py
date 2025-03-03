#WordIndex.py
#Name:Nomaan Ahmed 
#Date:3/1/25
#Assignment:Lab 6

def main():
    textFile = open("fish.txt", 'r')
    
    words = {} # Create an empty dictionary
    
    # Process the file line by line
    lineNum = 1
    for line in textFile:
        # Split the line into words
        wordList = line.strip().lower().split()
        
        # Clean up words by removing punctuation
        cleanWords = []
        for word in wordList:
            cleanWord = word.strip('.,!?:;()[]{}"\'-')
            if cleanWord:  # Only add non-empty words
                cleanWords.append(cleanWord)
        
        # Add each word to the dictionary with the current line number
        for word in cleanWords:
            if word in words:  # If word already exists in dictionary
                if lineNum not in words[word]:  # Only add line number if not already there
                    words[word].append(lineNum)
            else:  # Word not in dictionary yet
                words[word] = [lineNum]  # Create new entry with line number in a list
        
        lineNum += 1

if __name__ == '__main__':
    main()
