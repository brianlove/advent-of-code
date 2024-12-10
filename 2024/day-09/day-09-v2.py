#! /usr/bin/env python3

import argparse
import collections

parser = argparse.ArgumentParser("Day 9, v2")
parser.add_argument("infile", help="The input file")
args = parser.parse_args()

def part1(lines):
    print("\n\n~~ PART 1~~")
    pass


class FSNode:
    def __init__(self, addr, size, fileId):
        self.addr = addr
        self.size = size
        self.fileId = fileId
        self.hasMoved = False
        self.prev = None
        self.next = None

    def __str__(self):
        return f"FSNode(<{self.addr}::{self.size}>, {self.fileId})"

def part2(lines):
    print("\n\n~~ PART 2~~")
    rawInput = [int(x) for x in lines[0]]
    fileId = 0
    blockSize = rawInput[0]
    fsStart = FSNode(0, blockSize, fileId)
    currFile = fsStart
    nextIndex = blockSize

    for ix, digit in enumerate(rawInput):
        if ix == 0:
            continue
        fileId = None if (ix % 2 == 1) else ix // 2
        blockSize = digit
        newFile = FSNode(nextIndex, blockSize, fileId)
        newFile.prev = currFile
        currFile.next = newFile
        currFile = newFile
        nextIndex += blockSize

    fsEnd = currFile

    print("\n\nFile system start and end:")
    print("  start:", fsStart)
    print("  end:  ", fsEnd)

    firstFree = fsStart
    while firstFree.fileId is not None:
        firstFree = firstFree.next

    ## Relocate the files at the end to earlier places in the file system
    fileToRelocate = fsEnd
    while fileToRelocate.addr > 0:
        # print("\n\nRelocating file ", fileToRelocate)
        if fileToRelocate.fileId == None or fileToRelocate.hasMoved:
            fileToRelocate = fileToRelocate.prev
            continue
        isFileRelocated = False
        neededSpace = fileToRelocate.size

        ## Find the first empty space big enough for this file
        check = firstFree
        while check.next:
            # if check.addr > 20:
            #     break
            if check.addr >= fileToRelocate.addr:
                break
            # print("  checking ", check)
            if check.fileId == None and check.size >= neededSpace:
                ## Relocate!
                if check.size == neededSpace: ## Blocks are same size, so reuse the node
                    check.fileId = fileToRelocate.fileId
                    isFileRelocated = True
                    fileToRelocate.fileId = None
                    check.hasMoved = True
                    break
                else: ## There's extra space, so create a new empty node for the remainder
                    newNode = FSNode(check.addr + neededSpace, check.size - neededSpace, None)
                    check.size = neededSpace
                    check.fileId = fileToRelocate.fileId
                    newNode.prev = check
                    newNode.next = check.next
                    check.next.prev = newNode
                    check.next = newNode
                    fileToRelocate.fileId = None
                    isFileRelocated = True
                    check.hasMoved = True
                    break
            else: ## Not a candidate spot
                check = check.next

        fileToRelocate = fileToRelocate.prev
        if fileToRelocate is None or isFileRelocated:
            continue

        ## current --> current.next --> current.next.next
        ## c.n.prev    c.n.n.prev

        ## Consolidate free space:
        while firstFree.fileId is not None:
            firstFree = firstFree.next
        current = firstFree
        while current.next:
            current = current.next
            # print("Looking at ", current)
            ## if `current` and `current.next` are adjacent empty blocks, merge them
            if current.fileId is None and current.next and current.next.fileId is None:
                # print("Merging ", current, current.next)
                current.size = current.size + current.next.size
                if current.next.next:
                    current.next.next.prev = current
                current.next = current.next.next

    f = fsStart
    print("\nThe file system:")
    while f is not None:
        print("- ", f)
        f = f.next

    ## Calculate the filesystem's checksum
    checksum = 0
    current = fsStart
    while current:
        if current.fileId is not None:
            addresses = range(current.addr, current.addr+current.size)
            newChecksums = [addr * current.fileId for addr in addresses]
            checksum += sum(newChecksums)
        current = current.next
    print("Checksum:", checksum)


with open(args.infile) as file:
    lines = [line.rstrip() for line in file.readlines()]
    # part1(lines)

    part2(lines)
