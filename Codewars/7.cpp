#include <cinttypes>
#include <algorithm>
#include <string>

uint64_t descendingOrder(uint64_t a)
{
    std::string str = std::to_string(a);
    std::sort(str.begin(), str.end(), std::greater<char>());
    return std::stoull(str);
}