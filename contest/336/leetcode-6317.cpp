#include <vector>
#include <map>

class Solution{
    public:
        long long beautifulSubarrays(vector<int>& nums){
            map<int, int>pref;
            long long ans=0, x=0;
            pref[0] = 1;
            for(int i=0; i<nums.size(); i++){
                x ^= nums[i];
                if(pref.find(x)!=pref.end()) ans = ans + pref[x];
                pref[x]+=1;
            }
            return ans;
        }
};

// This worked!