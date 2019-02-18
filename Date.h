/*************************************************************************
 * AUTHOR             : John Zavala
 * STUDENT ID         : 100647
 * Assignment  #4     : Inheritance
 * CLASS              : CS1C
 * SECTION            : MTWTH  4:00-8:00
 * DUE DATE           : 6/1/2016
 * ***********************************************************************/

#include "header.h"
 //Date class
class date
{
public:
	date(); // constructor
	~date();// de-constructor

	//sets date
	void setDate(int month, int day, int year);

	//gets date
	int getDate();

	//prints date
	void printDate();

	//private variables
private:
	int dateMonth;
	int dateDay;
	int dateYear;


};
