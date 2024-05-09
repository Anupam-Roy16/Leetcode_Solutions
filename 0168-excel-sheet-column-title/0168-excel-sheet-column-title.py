class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        column_title = ""
        while columnNumber > 0:
            remainder = (columnNumber - 1) % 26
            column_title += chr(ord('A') + remainder)
            columnNumber = (columnNumber - 1) // 26
        return column_title[::-1]








        