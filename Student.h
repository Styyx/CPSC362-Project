/*************************************************************************
 * Assignment         : Group Project
 * CLASS              : CPSC 362
 * SECTION            : MW  8:00Am-9:50
 * ***********************************************************************/

#include "Header.h"
#include "Date.h"

 //student class
class student
{
public:

	//construtor
	student();
	//sets student name
	void setStudentName(string name);
	//sets id
	void setStudentId(int id);
	//sets phone nuber
	void setStudentPhoneNumber(string phoneNumber);
	//sets age
	void setStudentAge(int age);
	//sets gender
	void setStudentGender(char gender);
	//sets date
	void setDate(int month, int day, int year);
	//prints student
	void printStudent();

	//returns the student name
	string getStudentName();
	//returns the student id
	int getStudentId();
	//returns student phone number
	string getStudentPhoneNumber();
	//returns student age
	int getStudentAge();
	//returns student gender
	char getStudentGender();
	//returns the date
	date getDate();

	//student class variables
protected:
	string studentName;
	int studentId;
	string studentPhoneNumber;
	int studentAge;
	char studentGender;
	string studentDate;
	date myDate;


};
