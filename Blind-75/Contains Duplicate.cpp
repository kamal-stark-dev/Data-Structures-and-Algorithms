#include <iostream>
#include <vector>
#include <algorithm>
#include <unordered_set>
using namespace std;

// Brute Force - TC: O(n^2), SC: O(1)
bool containsDuplicate_BruteForce(vector<int>& nums) {
  int n = nums.size();

  for (int i = 0; i < n; i++) {
    for (int j = i + 1; j < n; j++) {
      if (nums[i] == nums[j])
        return true;
    }
  }
  return false;
}

// Sorting (Better) - TC: O(n logn), SC: O(logn) - due to internal soritng stack (no extra heap memory though)
bool containsDuplicate_Sorting(vector<int>& nums) {
  sort(nums.begin(), nums.end()); // O(n logn)
  
  int n = nums.size();
  for (int i = 1; i < n; i++) {
    if (nums[i] == nums[i - 1]) 
      return true;
  }
  return false;
}

// Optimal - TC: O(n), SC: O(n), Note: Worst Case TC: O(n^2) if hash collision occurs
bool containsDuplicate(vector<int>& nums) {
  unordered_set<int> st;

  for (int num: nums) {
    if (st.find(num) != st.end()) return true;
    st.insert(num);
  }
  return false;
}

// Compact way to write the same thing 
bool containsDuplicate_Compact(vector<int>& nums) {
  unordered_set<int> st(nums.begin(), nums.end());
  return st.size() != nums.size();
}

int main() {
  vector<int> nums = {1, 2, 3, 1};
  
  cout << "Contains Duplicates: " << (containsDuplicate_Compact(nums) ? "True" : "False") << "\n";

  return 0;
}
