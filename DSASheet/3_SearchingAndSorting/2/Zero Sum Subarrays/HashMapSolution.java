import java.io.*;
import java.util.*;

public class HashMapSolution {
    public static long findSubArray(long[] arr, int n){
        HashMap<Long, Integer> visitedSum = new HashMap();
        visitedSum.put(0L, 1);
        long currentSum = 0L;
        long result = 0;
        for (int i = 0; i < arr.length; i ++){
            currentSum += arr[i];
            int currentSumCount = visitedSum.getOrDefault(currentSum, 0);
            result += currentSumCount;
            visitedSum.put(currentSum, currentSumCount + 1);
        }
        return result;
    }
    public static void main(String[] args){
        long[] arr = {0, 0, 5, 5, 0, 0};
        System.out.println(findSubArray(arr, arr.length));


        
    }
}


