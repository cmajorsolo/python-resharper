class Solution:
    def convert(self, s, numRows):
        if len(s) == 0 or len(s) == 1:
            return s
        else:
            if len(s) < numRows:
                return s
            else:
                if numRows == 0 or numRows == 1:
                    return s
                elif numRows == 2:
                    firstRow = [element for index, element in enumerate(s) if index % 2 == 0]
                    secondRow = [element for index, element in enumerate(s) if index % 2 != 0]
                    result = firstRow + secondRow
                    result = ''.join(result)
                    # print(result)
                    return result
                elif numRows > 2:
                    result = []
                    magicNumber = numRows - 2 + numRows
                    magicNumberCopy = magicNumber
                    indexPlusOneArray = [magicNumber]
                    while magicNumber > 0:
                        magicNumber = magicNumber - 2
                        if magicNumber > 0:
                            indexPlusOneArray.append(magicNumber)
                        magicNumbersChild = magicNumberCopy - magicNumber
                        indexPlusOneArray.append(magicNumbersChild)
                    # print(indexPlusOneArray)

                    indexesByRow = []
                    for i in range(1, numRows + 1):
                        if i == 1 or i == numRows:
                            indexesByRow.append(i)
                            addingFactor = indexPlusOneArray.pop(0)
                            nextIndex = i + addingFactor
                            while nextIndex <= len(s):
                                indexesByRow.append(nextIndex)
                                nextIndex = nextIndex + addingFactor
                        else:
                            addingFactor = []
                            addingFactor.append(indexPlusOneArray.pop(0))
                            addingFactor.append(indexPlusOneArray.pop(0))
                            addingResult = i
                            indexesByRow.append(addingResult)
                            while addingResult < len(s):
                                for item in addingFactor:
                                    addingResult = addingResult + item
                                    if addingResult <= len(s):
                                        indexesByRow.append(addingResult)
                    # print(indexesByRow)
                    for index in indexesByRow:
                        result.append(s[index - 1])
                    # print("".join(result))
                    return "".join(result)
