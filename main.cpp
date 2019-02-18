#include<iostream>
#include <iomanip>
#include "Header.h"
#include "Student.h"

using namespace std;

int main()
{

	// my student class variable
	student myStudent;
	date myDate;
	int newMonth;
	int newDay; 
	int newyear;
	string newName;
	int newId;
	string newPhone;
	int newAge;
	char newGender;

	//enum for menu
	MENU myMenu;

	//user input for menu
	int input = 0;

	//displays a menu
	DisplayMenu();

	cin >> input;
	cin.ignore(1000, '\n');

	//setting myMenu = input
	myMenu = MENU(input);

	cout << "testing input: " << input << endl;

	while (input != EXIT)
	{
		switch (input)
		{
		case ADD_STUDENT: 
			cout << "Adding a new student" << endl;
			cout << "Enter students name: ";
			getline(cin, newName);
			myStudent.setStudentName(newName);
			cout << endl;
			cout << "Enter students Id: ";
			cin >> newId;
			cin.ignore(1000, '\n');
			myStudent.setStudentId(newId);
			cout << endl;
			cout << "Enter students phone number: ";
			getline(cin, newPhone);
			myStudent.setStudentPhoneNumber(newPhone);
			cout << endl;
			cout << "Enter students age: ";
			cin >> newAge;
			cin.ignore(1000, '\n');
			myStudent.setStudentAge(newAge);
			cout << endl;
			cout << "Enter student gender: ";
			cin.get(newGender);
			myStudent.setStudentGender(newGender);
			cout << endl;
			cout << "Enter date  (month day year): ";
			cin >> newMonth >> newDay >> newyear;
			myStudent.setDate(newMonth, newDay, newyear);
		
			cout << "Succesfully added student" << endl;
			break;
		case EXIT: break;;

		}
		
		//displays a menu
		DisplayMenu();
		cin >> input;
		cin.ignore(1000, '\n');

	}

	//testing
	cout << "Testing if adding student works" << endl;
	myStudent.printStudent();
	cout << endl;


	//testing
	cout << "testing" << endl;
	myStudent.setStudentName("John");
	myStudent.setStudentId(12345);
	myStudent.setStudentPhoneNumber("949-123-4567");
	myStudent.setStudentAge(20);
	myStudent.setStudentGender('M');
	myStudent.setDate(4, 5, 2019);
	myStudent.printStudent();






	system("pause");
	return 0;
}