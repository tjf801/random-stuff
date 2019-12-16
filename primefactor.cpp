#include <iostream>

int main(){
	unsigned long long int n;
	std::cin >> n;
	if (n >= 18446744073709551615) {
		std::cout << "too big!" << std::endl;
	}
	unsigned long long int i = 2;
	while (n!=1) {
		if (n % i == 0) {
			std::cout << (i) << std::endl;
			n = n / i;
		} else {
			i++;
		}
	}
	system("PAUSE");
}