You have been given 3 integers - l, r and k. Find how many numbers between l and r (both inclusive) are divisible by k. You do not need to print these numbers, you just have to find their count.

Input Format
The first and only line of input contains 3 space separated integers l, r and k.

Output Format
Print the required answer on a single line.

Constraints
 
 1 <= l <= r <= 1000
 1 <= k <= 1000
 
 
 
 
 
 SOLUTION:
---------------------------------------------------------------------------------- 
 PYTHON 3
 
 # Write your code here
count = 0
l,r,k = map(int,input().split())
for i in range(l,r+1):
    if i%k == 0:
        count = count +1
print(count)

------------------------------------------------------------------------------------

C++


#include <iostream>
using namespace std;

int main()
{
    int l,k,r,count=0;
    cin>>l;
    cin>k;
    cin>>r;
    for(int i=l;i<r;i++)
    {
        if(l%k==0)
        {
            count+=1;
        
        }
    }
    cout<<count;
    return 0;
}

-----------------------------------------------------------------------------------------
