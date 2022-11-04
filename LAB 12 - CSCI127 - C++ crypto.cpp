//Name: Drew Zambelli
//Email: drew.zambelli04@myhunter.cuny.edu
//Date: 11/22/21
//My first program in C++

#include <iostream>
#include <iomanip>
using namespace std;

float main()
{
  float amount;
  float b, e, d;
  float result, results, resultz;
  b = 31,901.19
  e = 1,901.54
  d = 0.179733
  cout << "Enter amount in cryptocurrency:";
  cin >> amount
  result = b * amount
  results = e * amount
  resultz = d * amount
  cout << fixed << setprecision(2);
  cout << amount << "BTC in USD:" << result;
  cout << amount << "ETH in USD:" << results;
  cout << amount << "DOGE in USD:" << resultz;
  return 0;
}