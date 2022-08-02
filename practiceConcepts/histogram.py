class Solution:
    def getMaxArea(self,histogram):
        #code here
        max = 0
        for i in range(len(histogram)):
            size = histogram[i]
            print("new val: ", size, "index i: ", i)
            if i < len(histogram):
                print("valuecheck:")
                for j in range(i+1, len(histogram)):
                    print(histogram[j])
                    if histogram[j] >= size:
                        count+=1
                    else: 
                        break
            if i >= 1:
                print("valuecheck:")
                for k in range(i-1, 0):
                    print(histogram[k])
                    if histogram[k] >= size: 
                        count+=1
                    else: 
                        break
            area = size * count
            if max< area: 
                max = area
            
        return max