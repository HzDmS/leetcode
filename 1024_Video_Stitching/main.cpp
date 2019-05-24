class Solution {
public:
    
    // greedy algorithm
    // time complexity: O(N + NlogN)
    // space complexity: O(1)
    
    int videoStitching(vector<vector<int>>& clips, int T) {
        sort(clips.begin(), clips.end());
        
        int res = 0;
        
        for (int i = 0, start = 0, end = 0;
             start < T;
             start = end, res++) {
            while (i < clips.size() && clips[i][0] <= start && end <= T) {
                end = max(end, clips[i][1]);
                i++;
            }
            if (end == start) return -1;
        }
        return res;
    }
    
// Dynamic Programming
// time complexity: O(NT), where N is the size of clips.
// space complexity: O(T + 1);
//     int videoStitching(vector<vector<int>>& clips, int T) {
//         vector<int> cuts(T + 1, T + 1);
//         int n = clips.size();
        
//         cuts[0] = 0;
//         for (int i = 1; i <= T; i++) {
//             for (auto c : clips) {
//                 if (i >= c[0] && i <= c[1]) {
//                     cuts[i] = min(cuts[i], cuts[c[0]] + 1);
//                 }
//             }
//         }
//         return cuts[T] == T + 1 ? -1 : cuts[T];
//     }
};
