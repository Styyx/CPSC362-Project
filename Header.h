/*************************************************************************
 * Assignment         : Group Project
 * CLASS              : CPSC 362
 * SECTION            : MW  8:00Am-9:50
 * ***********************************************************************/

#ifndef MYHEADER_H_
#define MYHEADER_H_

#include <iostream>
#include <iomanip>
#include<string>
#include<limits>

using namespace std;

//enum for menu
enum MENU
{
	EXIT = 0,
	ADD_STUDENT = 1,
	UPDATE_COURSE = 2,
	TRACK_LOAN = 3,
	TRACK_RETURN = 4,
	VERIFY_BOOKS = 5
};



/**************************************************************************
 * DisplayMenu
 * 		This function outputs the menu
 *************************************************************************/
//displays menu
void DisplayMenu();

//validate input function
//int ValidateIntRange(const string PROMPT, const int BEGIN_RANGE,
	//const int END_RANGE);

#endif /* HEADER_H_ */
