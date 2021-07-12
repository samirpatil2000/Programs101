// #include<iostream>
#include <bits/stdc++.h>
using namespace std;

class MedianFinder{
public:

    priority_queue<int> maxHeap;
    priority_queue<int, vector<int>, greater<int> > minHeap;

    void addNum(int num) {
        if (maxHeap.empty() || maxHeap.top()>=num){
            maxHeap.push(num);
        }else{
            minHeap.push(num);
        }
        balance();
    }
    void balance(){
        if (maxHeap.size()>minHeap.size()+1){
            minHeap.push(maxHeap.top());
            maxHeap.pop();
        }else if(maxHeap.size()>minHeap.size()+1){
            maxHeap.push(minHeap.top())
            minHeap.pop()
        }
    }
    double findMedian(){
        if (maxHeap.size()==minHeap.size()){
            return (maxHeap.top()+minHeap.top())/2.0
        }else{
            if(maxHeap.size() > minHeap.size()){
                return maxHeap.top();
            }else{
                return minHeap.top();
            }
        }
    }

}

int main(){
    obj=MedianFinder();
    obj.addNum(1);
    obj.addNum(2);
    obj.addNum(3);
    obj.addNum(4);
    cout<<obj.findMedian<<endl;
    // /Library/Developer/CommandLineTools/usr/include/c++/v1
}