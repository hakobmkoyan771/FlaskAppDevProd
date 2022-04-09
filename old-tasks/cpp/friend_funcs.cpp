#include <iostream>

class Man {
	private:
		int memb_1;
		friend int fr(Man);
};

int fr(Man tp) {
	tp.memb_1 = 54;
	int num = tp.memb_1 + 6;
	return num;
}

int main() {
	Man man;
	int n = fr(man);
	std::cout << n << std::endl;

}
