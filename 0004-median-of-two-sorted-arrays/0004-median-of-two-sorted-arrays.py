class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        result=nums1+nums2
        new_result=sorted(result)
        if len(new_result)%2!=0:
            index=int((0+len(new_result))/2)
            return new_result[index]
        else:
            index1=int((0+len(new_result))/2)
            ans=float((new_result[index1-1]+new_result[index1]))
            ans/=2
            return ans

        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        