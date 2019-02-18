/*************************************************************************
 * Assignment         : Group Project
 * CLASS              : CPSC 362
 * SECTION            : MW  8:00Am-9:50
 * ***********************************************************************/

#include "Header.h"
 /**************************************************************************
  *
  * FUNCTION DisplayMenu
  *_________________________________________________________________________
  *	Display the menu to the users to choose from.
  *_________________________________________________________________________
  * PRE-CONDITIONS
  *  none
  *
  * POST CONDITIONS
  * 	Displays the menu to the user screen
  *
  **************************************************************************/
  //displays menu
void DisplayMenu()
{
	cout << setw(50) << "Welcome to Books Advantage Web App" << endl << endl;
	cout << "Please select an option below (input a number between 0-5 )" << endl;

	cout << "1 - Add Student" << endl;
	cout << "2 - Update Courses" << endl;
	cout << "3 - Track student book loans" << endl;
	cout << "4 - Track student book returns" << endl;
	cout << "5-  Verify loaned books to students" << endl;
	cout << "0 - EXIT" << endl << endl;

}
