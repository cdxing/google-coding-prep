# LC 739 - Daily Temperatures
#
# Given an array of daily temperatures, return an array where
# answer[i] is the number of days until a warmer temperature.
# If no warmer day exists, answer[i] = 0.
#
# Example:
# Input:  [73,74,75,71,69,72,76,73]
# Output: [1, 1, 4, 2, 1, 1, 0, 0]
#
# Approach: monotonic stack
# Stack stores indices of days still waiting for a warmer day

def dailyTemperatures(temperatures):
    output = []
    stack = []
    for i in range(len(temperatures)):
        output.append(0)
        while stack  and temperatures[i] > temperatures[stack[-1]]:
            j = stack.pop()
            output[j] = i - j
        stack.append(i)
    return output

print(dailyTemperatures([73,74,75,71,69,72,76,73]))  # [1,1,4,2,1,1,0,0]
print(dailyTemperatures([30,40,50,60]))               # [1,1,1,0]
print(dailyTemperatures([30,60,90]))                   # [1,1,0]
