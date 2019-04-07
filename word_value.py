#!/usr/bin/python3
'''
    ## NOTE ##
    This code assume that inserted text file is English words and have only 1 word in each line
    So it split each line by '\n' and convert each lower case alphabet to ASCII decimal integer then subtract by 96

    Tested text file :
        https://github.com/dwyl/english-words/blob/master/words_alpha.txt
'''

#   Dictionary text file name 
inputFileName = 'words_alpha.txt'
outputFileName = 'output.txt'

print( 'Reading file "{}" to generate output in "{}" ...'.format( inputFileName, outputFileName ) )

#   Read the file and split each line to lower case string
with open( inputFileName ) as inputFile:
    textFile = inputFile.read().lower().split( '\n' )

#   Initialize output list
outputList = []

#   Loop each word line in text file
for word in textFile:

    #   Set initial value for word value
    wordValue = 0

    #   Loop each alphabet in word
    for alphabet in word:

        #   Convert alphabet to integer value and subtract by 96, then add to word value
        alphabetValue = ord( alphabet ) - 96
        wordValue = wordValue + alphabetValue
    
    #   If word value is equal to 100, append its to output list
    if( wordValue == 100 ):
        outputList.append( word )

#   Write word from output list to a file
with open( outputFileName, 'w' ) as outputFile:
    for word in outputList:
        outputFile.write( '{}\n'.format( word ) )
