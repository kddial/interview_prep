class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        # only 1 row
        if(numRows == 1):
            return s

        # construct rows array
        rows = []
        for i in range(numRows):
            rows.append("")

        increase_row = True
        r_index = 0
        i = 0
        while(i < len(s)):
            # append character to row
            rows[r_index] = rows[r_index] + s[i]

            # row ordering logic for zig zag
            if r_index == numRows - 1:
                increase_row = False
            elif r_index == 0:
                increase_row = True

            # setup next row
            if increase_row:
                r_index = r_index + 1
            else:
                r_index = r_index - 1

            i = i + 1

        # contruct output string
        output = ""

        for row in rows:
            output = output + row
        return output
