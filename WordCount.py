#WordCount.py
#Name:Nomaan Ahmed
#Date:3/1/25
#Assignment:Lab 6 

def main():
        textFile = open("gettysberg.txt", 'r')
        lineCount = 0
        wordCount = 0
        letterCount = 0

        for line in textFile:
            lineCount += 1
            words = line.split()
            wordCount += len(words)
            letterCount += len(line)  

        textFile.close() 

        print("Lines:", lineCount)
        print("Words:", wordCount)

if __name__ == '__main__':
    main()