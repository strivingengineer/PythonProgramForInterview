maintainer = 'strivingengineer'
'''
Leetcode 981. Time Based Key-Value Store
https://leetcode.com/problems/time-based-key-value-store/
Design a time-based key-value data structure that can store multiple values 
for the same key at different time stamps and retrieve the key's value at a certain timestamp.

Implement the TimeMap class:
TimeMap() Initializes the object of the data structure.
void set(String key, String value, int timestamp) Stores the key key 
with the value value at the given time timestamp.
String get(String key, int timestamp) Returns a value such that set
was called previously, with timestamp_prev <= timestamp. If there are multiple such values,
it returns the value associated with the largest timestamp_prev. If there are no values, it returns "".
 
Example 1:
Input
["TimeMap", "set", "get", "get", "set", "get", "get"]
[[], ["foo", "bar", 1], ["foo", 1], ["foo", 3], ["foo", "bar2", 4], ["foo", 4], ["foo", 5]]
Output
[null, null, "bar", "bar", null, "bar2", "bar2"]

Explanation
TimeMap timeMap = new TimeMap();
timeMap.set("foo", "bar", 1);  // store the key "foo" and value "bar" along with timestamp = 1.
timeMap.get("foo", 1);         // return "bar"
timeMap.get("foo", 3);         // return "bar", since there is no value corresponding to foo at 
timestamp 3 and timestamp 2, then the only value is at timestamp 1 is "bar".
timeMap.set("foo", "bar2", 4); // store the key "foo" and value "bar2" along with timestamp = 4.
timeMap.get("foo", 4);         // return "bar2"
timeMap.get("foo", 5);         // return "bar2"

Constraints:
1 <= key.length, value.length <= 100
key and value consist of lowercase English letters and digits.
1 <= timestamp <= 107
All the timestamps timestamp of set are strictly increasing.
At most 2 * 105 calls will be made to set and get.

Approach:Simple solution will be a linear search solution on values and return the value, it will be a O(n) solution.
Since we have the timestmap in increasing order so because of which we can use binary search.
We can store the key and values as list of list with value & timestamp in it.
If we can find any key in get operation then we should check if the current value is less than equal to timestamp
given if yes we should store the value as potential answer since we have to handle the case if key with current
timestamp is not present then we should return the closet timestamp <= timestamp given in query.
Time/ Space Complexity: O(nlog(n))/O(1)
'''


class TimeMap:

    def __init__(self):
        self.keyvaluestore = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.keyvaluestore:
            self.keyvaluestore[key] = []

        self.keyvaluestore[key].append([value, timestamp])

    def get(self, key: str, timestamp: int) -> str:

        res = ""
        values = self.keyvaluestore.get(key, [])
        left, right = 0, len(values) - 1
        while left <= right:
            mid = (left + right) // 2
            if values[mid][1] <= timestamp:
                res = values[mid][0]
                left = mid + 1
            else:
                right = mid - 1

        return res