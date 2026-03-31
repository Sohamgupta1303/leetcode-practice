class Solution {
public:
    struct Compare {
        bool operator()(const vector<int>& a,
                        const vector<int>& b) const {
            int distA = a[0]*a[0] + a[1]*a[1];
            int distB = b[0] * b[0] + b[1]*b[1];
            return distA < distB;  // max-heap
        }   
    };
    vector<vector<int>> kClosest(vector<vector<int>>& points, int k) {
        using namespace std;
        priority_queue<vector<int>, vector<vector<int>>, Compare> pq;
        for (int i = 0; i < points.size(); i++) {
            vector<int> point = points[i];
            pq.push(point);
            while(pq.size() > k){
                pq.pop();
            }
        }
        vector<vector<int>> ret;
        int size = 0;
        while(!pq.empty() && size < k) {
            ret.push_back(pq.top());
            pq.pop();
            size++;
        }
        return ret;
    }
};