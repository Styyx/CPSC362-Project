/*************************************************************************
 * Assignment         : Group Project
 * CLASS              : CPSC 362
 * SECTION            : MW  8:00Am-9:50
 * ***********************************************************************/

#include "Header.h"
#include "Student.h"

 //constructor
student::student()
{
	//initializes variable
	studentName = " ";
	studentId = 0;
	studentPhoneNumber = " ";
	studentAge = 0;
	studentGender = ' ';
	studentDate = " ";
	myDate.setDate(0, 0, 0);


}

//sets name
void student::setStudentName(string name)
{
	studentName = name;
}
//sets id
void student::setStudentId(int id)
{
	studentId = id;
}
//sets phone
void student::setStudentPhoneNumber(string phoneNumber)
{
	studentPhoneNumber = phoneNumber;
}
//sets age
void student::setStudentAge(int age)
{
	studentAge = age;
}
//sets gender
void student::setStudentGender(char gender)
{
	studentGender = gender;
}

//gets name
string student::getStudentName()
{
	return studentName;
}
//gets  id
int student::getStudentId()
{
	return studentId;
}
//gets phone
string student::getStudentPhoneNumber()
{
	return studentPhoneNumber;
}
//gets age
int student::getStudentAge()
{
	return studentAge;
}
//gets gender
char student::getStudentGender()
{
	return studentGender;
}

//sets date
void student::setDate(int month, int day, int year)
{
	myDate.setDate(month, day, year);
}
//gets date
date student::getDate()
{
	return myDate;
}
//prints student
void student::printStudent()
{
	cout << right;
	cout << "Student name: " << studentName << endl;
	cout << "Student Id: " << studentId << endl;
	cout << "Student Phone: " << studentPhoneNumber << endl;
	cout << "Stuent Age: " << studentAge << endl;
	cout << "Student Gender: " << studentGender << endl;
	cout << "Date: " << studentDate;
	myDate.printDate();
	cout << endl;
}
