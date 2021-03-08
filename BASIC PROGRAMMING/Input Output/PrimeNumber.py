You are given an integer N. You need to print the series of all prime numbers till N.

Input Format

The first and only line of the input contains a single integer N denoting the number till where you need to find the series of prime number.

Output Format

Print the desired output in single line separated by spaces.

Constraints

1<=N<=1000



SLOUTION:


IN C++


#include <bits/stdc++.h>
using namespace std;

void SieveOfEratosthenes(int n)
{
	// Create a boolean array "prime[0..n]" and initialize
	// all entries it as true. A value in prime[i] will
	// finally be false if i is Not a prime, else true.
	bool prime[n+1];
	memset(prime, true, sizeof(prime));

	for (int p=2; p*p<=n; p++)
	{
		// If prime[p] is not changed, then it is a prime
		if (prime[p] == true)
		{
			// Update all multiples of p
			for (int i=p*2; i<=n; i += p)
				prime[i] = false;
		}
	}

	// Print all prime numbers
	for (int p=2; p<=n; p++)
	if (prime[p])
		cout << p << " ";
}

// Driver Program to test above function
int main()
{
	int n;
	/*cout << "Following are the prime numbers smaller "
		<< " than or equal to " << n << endl;
	*/
	cin>>n;
	SieveOfEratosthenes(n);
	return 0;
}






IN PYTHON 3