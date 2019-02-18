/*************************************************************************
 * Assignment         : Group Project
 * CLASS              : CPSC 362
 * SECTION            : MW  8:00Am-9:50
 * ***********************************************************************/
#include "Header.h"
#include "Date.h"
 //CONSTRUCTOR
date::date()
{
	//INITIALIZING VARIABLES
	dateMonth = 0;
	dateDay = 0;
	dateYear = 0;

}
//DECONSTRUCTOR
date::~date()
{

}
//SETS DATE
void date::setDate(int month,
	int day,
	int year)
{
	dateMonth = month;
	dateDay = day;
	dateYear = year;
}
//GETS DATE
int date::getDate()
{
	return dateMonth;
	return dateDay;
	return dateYear;
}
//PRINTS DATE
void date::printDate()
{
	cout << dateMonth << "/" << dateDay << "/" << dateYear;
}
