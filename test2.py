#!/bin/python3

import math
import os
import random
import re
import sys
import bisect



#
# Complete the 'getMinTime' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY task_memory
#  2. INTEGER_ARRAY task_type
#  3. INTEGER max_memory
#

def getMinTime(task_memory, task_type, max_memory):
    n = len(task_memory)
    taskToPosition = {}
    tasksGroupedByType = []
    time = 0
    for i in range(n):
        if task_type[i] in taskToPosition:
            bisect.insort(tasksGroupedByType[taskToPosition[task_type[i]]], task_memory[i])
        else:
            taskToPosition[task_type[i]] = len(tasksGroupedByType)
            tasksGroupedByType.append([task_memory[i]])
            
    for tasks in tasksGroupedByType:
        singleTasks = []
        for taskA in reversed(tasks):
            added_to_group = False
            limit = binary_search_first_below(singleTasks, max_memory - taskA)
            if limit != None:
                singleTasks.pop(limit)
                time += 1
                added_to_group = True

            if not added_to_group:
                singleTasks.append(taskA)
        time += len(singleTasks)

    return time

def binary_search_first_below(arr, target):
    low, high = 0, len(arr) - 1
    result = None

    while low <= high:
        mid = (low + high) // 2

        if arr[mid] <= target:
            result = mid
            high = mid - 1
        else:
            low = mid + 1

    return result


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    task_memory_count = int(input().strip())

    task_memory = []

    for _ in range(task_memory_count):
        task_memory_item = int(input().strip())
        task_memory.append(task_memory_item)

    task_type_count = int(input().strip())

    task_type = []

    for _ in range(task_type_count):
        task_type_item = int(input().strip())
        task_type.append(task_type_item)

    max_memory = int(input().strip())

    result = getMinTime(task_memory, task_type, max_memory)

    fptr.write(str(result) + '\n')

    fptr.close()