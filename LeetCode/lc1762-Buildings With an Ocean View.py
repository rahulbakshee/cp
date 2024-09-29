heights = [4,3,2,1]

def building(heights):
	maxx = 0
	result = []
	for i in range(len(heights)-1, -1, -1):
		if maxx > heights[i]:
			continue
		else: # maxx < heights[i]
			result.append(i)
			maxx = heights[i]

	return result[::-1]


print(building(heights))
