#include "stdafx.h"
#include "stdlib.h"
#include <string>
#include <iomanip>  
#include <iostream>
#include <fstream>
#include <sstream>
using namespace std;

int main()
{
	ifstream fin("D:\\bysj\\DataSet\\NONCODE V5\\NONCODEv5_human.lncRNA\\NONCODEv5_human.lncRNA2.exp", ios::in);
	ofstream fout("D:\\bysj\\DataSet\\NONCODE V5\\NONCODEv5_human.lncRNA\\NONCODEv5_human.lncRNA.exp", ios::app);
	if (!fin) {
		printf("The file is not exist!");
		return -1;
	}
	string line;
	while(getline(fin, line))
	{
		stringstream ss(line);
		string token;
		float token1;
		ss >> token;
		cout << token << "\n";
		fout << token<<"\t";
		while (ss >> token1){
			fout << setprecision(6) << token1<<"\t";
			
			}
		fout << endl;
		}	
	 fin.close();
	 fout.close();
	system("pause");
	return 0;
}
