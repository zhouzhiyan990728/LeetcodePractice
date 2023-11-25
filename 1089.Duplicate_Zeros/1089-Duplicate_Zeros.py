class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        index = 0;
        length = len(arr);
        while index<length-1:
            if arr[index] == 0:
                new_index = length-1;
                while new_index > index+1:
                    arr[new_index] = arr[new_index-1];
                    new_index -= 1;
                arr[index+1] = 0;
                index += 2;
            else:
                index += 1;