class Solution:
    def unionArray(self, nums1, nums2):

        n = len(nums1)
        m = len(nums2)
        union = []
        i,j = 0,0

        def addTo(val):
            if not union or union[-1] != val:
                union.append(val)

        while i <n and j < m:
            if nums1[i] < nums2[j]:
                addTo(nums1[i])
                i+=1
            elif nums1[i] > nums2[j]:
                addTo(nums2[j])
                j += 1
            else:
                addTo(nums1[i])
                i += 1
                j += 1

        while i < n:
            addTo(nums1[i])
            i += 1

        # Step 3: If there are leftovers in nums2, add them
        while j < m:
            addTo(nums2[j])
            j += 1

        return union