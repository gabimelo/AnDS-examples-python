'''
@ author: Brian Ezra, Gabriela Melo
@ since: 15/ 05/ 2015
@ modified: 18/ 05/ 2015
'''


def merge(left, right):
    '''
    merge part of the merge sort, uses built in list
    :param left: list of list
    :param right: list of list
    :return: sorted list
    :complexity: O(N): where N is len(left) + len(right)
    '''
    tmp = []
    i = 0
    j = 0
    while len(left) > 0 and len(right) > 0:
        try:
            if right[j][1] <= left[i][1]:
                tmp.append(right[0])
                right.__delitem__(0)            # serve from right list
            elif left[i] < right[j]:
                tmp.append(left[0])
                left.__delitem__(0)             # serve from left list
        except IndexError:
            return 'Need list of list as argument'
    try:
        while len(left) > 0:                        # serve all remaining items if any(either of left or right must be \
            tmp. append(left[0])                    # empty at this point)
            left.__delitem__(0)
        while len(right)> 0:                        # serve all remaining items if any ^
            tmp.append((right[0]))
            right.__delitem__(0)
    except TypeError:
        return -1
    return tmp


def merge_sort(a_list2):
    '''
    a specialized merge sort algorithm that splits and ascend-sorts given list of list according to the second element
    of each of the list's elements recursively, uses built in list
    :param a_list2: a LIST OF LIST
    :return: sorted list
    :complexity: O(Nlog(N)) : logN from splitting the list, N from merge
    '''
    if len(a_list2) == 1:
        return a_list2
    mid = int(len(a_list2)//2)

    left = merge_sort(a_list2[0: mid])
    right = merge_sort(a_list2[mid: len(a_list2)])      # split the list(right side)
    try:
        tmp = merge(left, right)                            # merge the 2 parts
    except (IndexError, TypeError):
        return 'Need list of list as argument'
    return tmp


def test_list_mergesort():
    print('testing function merge_sort')
    the_list2 = []
    for i in range(26):
        the_list = []
        the_list.append(str(chr(97 + i)))
        the_list.append(20 - i)
        the_list2.append(the_list)
    case1actual = []
    for i in range(len(the_list2)):
        case1actual.append(the_list2[-i-1])
    case1 = merge_sort(the_list2)
    for i in range(len(case1)):
        if case1[i] == case1actual[i]:
            pass
        else:
            print('False', case1, case1actual)
    print('Pass')
    print('testing merge_sort error handling')
    case2 = merge_sort([1,2,3,4,5])
    if case2 == 'Need list of list as argument':
        print('Pass')
    else:
        print('Fail', case2)
    print('finished testing merge_sort')


if __name__ == '__main__':
    test_list_mergesort()
