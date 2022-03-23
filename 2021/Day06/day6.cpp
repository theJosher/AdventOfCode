//usr/bin/make -s "${0%.*}" CFLAGS="-O3 -Wall -Werror" && ./"${0%.*}" "$@"; s=$?; exit $s
#include <iostream>
#include <cstdint>
#include <algorithm>
#include <array>
#include <iterator>
using namespace std;

int64_t simulate_fish(int_fast32_t *input, size_t length_input, int32_t days)
{
  std::array<int64_t, 9> fish = {0, 0, 0, 0, 0, 0, 0, 0, 0}; // Means initialize all array elements to 0 in an array of size 9

  for (size_t i = 0; i < length_input; i++)
  {
    fish[input[i]]++;
  }

  for (int d = 0; d < days; d++)
  {
    int64_t carry = fish[0];
    for (size_t i = 0; i < fish.size() - 1; i++)
    {
      fish[i] = fish[i + 1];
    }

    fish[6] += carry;
    fish[8] = carry;
  }

  int64_t total_fish = 0;
  for (size_t i = 0; i < fish.size(); i++)
  {
    total_fish += fish[i];
  }
  return total_fish;
}

int main()
{
  // 3,4,3,1,2
  int_fast32_t input[] = {3,4,3,1,2};
  size_t length_input = sizeof(input) / sizeof(input[0]);

  int64_t total_fish = simulate_fish(input, length_input, 80);

  cout
      << "Total fish: " << total_fish << "\n";

  return 0;
}