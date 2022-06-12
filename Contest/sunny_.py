
# def fun(k):
    # len_s=len(s)
    # arr=[0]*len_s
    # for i in range(len_s):
    #     arr[i]=ord(s[i])-ord("a")
    # len_e=len(e)
    # i=0
    # result=""
    # while i<len_e:
    #     result+=chr(((ord(e[i])+arr[i%len_s])-ord("a"))%26+ord("a"))
    #     i+=1
    # return result
    # int n=k.length;
    #     long[] ls=new long[n];
    #     for(int i=0;i<n;i++){
    #         for(int j=1;j<k[i];j++){
    #             if(k[i]%j==0){
    #                 ls[i]+=j;
    #                 //ls[i]+=k[i]/j;
                    
    #             }
                
    #         }
    #         ls[i]+=k[i];
    #     }
    #     return ls;
    # n = len(k)
    # result = [0]*n
    # for i in range(n):
    #     for j in range(1, k[i]):
    #         if k[i]%j == 0:
    #             result[i] += j
    #     result[i] += k[i]
    # return result


x=[2,3,7]
y=[4,-6,8]

def get_area(x,y):
    
    
    area_of_trangle = abs(0.5 * ( (x[0]*(y[1]-y[2])) + (x[1]*(y[2]-y[0])) + (x[2]*(y[0]-y[1]))))
    return int(area_of_trangle)


        
x=[0,4,7]
y=[0,8, 6]
print(get_area(x, y))