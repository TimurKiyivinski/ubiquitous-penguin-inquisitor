#!/bin/env python3
import argparse

def main(args):
    # Command line arguments
    inputString = args.input
    outputName = args.file
    setVerbose = args.verbose
    
    print('Input string: %s' % inputString)

    # Generate ascii string
    outputRaw = list(ord(char) for char in inputString)

    # Print ascii string
    if setVerbose:
        print('Raw ASCII:')
        print(outputRaw)

    # Generate brainfuck string
    outputString = ''
    for asciiChar in outputRaw:
        for i in range(0, asciiChar):
            outputString += '+'
        outputString += '.[-]'

    # Print brainfuck string
    if setVerbose:
        print(outputString)

    # Save file
    outputFile = open(outputName, 'w')
    outputFile.write(outputString)
    outputFile.close()

    pass

# Run main if not loaded as a module
if __name__ == '__main__':
    # Create a parser to handle command line arguments
    parser = argparse.ArgumentParser(description='Converts strings into Brainfuck.')
    parser.add_argument('-i', '--input', help='Input string', required=True)
    parser.add_argument('-f', '--file', help='Output brainfuck file', required=True)
    parser.add_argument('-v', '--verbose', help='Verbose logging', action='store_true')
    args = parser.parse_args()
    # Call the main
    quit(main(args))
