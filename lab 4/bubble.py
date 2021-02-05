def bubble_sort(nums, nums1):
    swapped = True
    while swapped:
        swapped = False
        for i in range(len(nums) - 1):
            if nums[i] > nums[i + 1]:
                # Меняем элементы
                nums[i], nums[i + 1] = nums[i + 1], nums[i]
                nums1[i], nums1[i + 1] = nums1[i + 1], nums1[i]
                # Устанавливаем swapped в True для следующей итерации
                swapped = True