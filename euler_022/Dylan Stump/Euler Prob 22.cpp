#include "stdafx.h"
#include <iostream>
#include <fstream>
#include <string>
#include <vector>

using namespace std;
ifstream inFS;

int main() {
	//declare variables and vectors
	vector <string> unsorted;
	vector <string> sorted;
	bool sort = false;
	string str;
	long double totalScore = 0;
	long double wordScore = 0;

	//get names from text doc into unsorted vector
	inFS.open("p022_names.txt");
	while (inFS >> str) {
		unsorted.push_back(str);
	}
	inFS.close();

	//sort unsorted vector into sorted vector
	sorted.push_back(unsorted.at(0));
	for (int i = 1; i < unsorted.size(); i++) {
		for (int j = 0; j < sorted.size(); j++) {
			if (unsorted.at(i).compare(sorted.at(j)) < 0) {
				sorted.insert(sorted.begin() + j, unsorted.at(i));
				sort = true;
				break;
			}
		}
		if (!sort) {
			sorted.push_back(unsorted.at(i));
		}
		sort = false;
	}

	//mult chars and vector postion and add to total score
	for (int i = 0; i < sorted.size(); i++){
		for (int j = 0; j < sorted.at(i).length(); j++) {
			wordScore += sorted.at(i).at(j) - 64;
		}
		totalScore += wordScore*(i + 1);
		wordScore = 0;
	}
	cout << to_string(totalScore) << endl;
	system("pause");
	return 0;
}
