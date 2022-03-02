import unittest
from unittest import TestCase
from unittest.mock import patch, call

import timesheets

class TestTimesheet(TestCase):
    """ mock the user input and for it to return a value to use for testing 
        test logic funtions, finish total hours. mock minimum.
    """

    @patch('builtins.input', side_effect=['2'])  # list a mock input here though side_effct, could be a list of inputs tried.
    def test_get_hours_for_day(self, mock_input):
        hours = timesheets.get_hours_for_day('Monday')  # testing the input is checking correctly housrs entered.
        self.assertEqual(2, hours) 


    @patch('builtins.input', side_effect=['cat', 'fish', '', '123birdy', 'pizza1234',  '2'])  # list of mock inputs here
    def test_get_hours_for_day_non_numeric(self, mock_input):
        hours = timesheets.get_hours_for_day('Monday')  # testing the input is checking correctly housrs entered.
        self.assertEqual(2, hours)     

    @patch('builtins.input', side_effect=[ '-12', '-1234',  '8'])  # list of mock neagative inputs here
    def test_get_hours_for_day_number_range_negative(self, mock_input):
        hours = timesheets.get_hours_for_day('Monday')  # testing the input is checking correctly housrs entered.
        self.assertEqual(8, hours)  
   

    @patch('builtins.input', side_effect=[ '120', '1234',  '8'])  # list of mock inputs here
    def test_get_hours_for_day_range_greater_than_24(self, mock_input):
        hours = timesheets.get_hours_for_day('Monday')  # testing the input is checking correctly housrs entered.
        self.assertEqual(8, hours)  


    @patch('builtins.input', side_effect=[ '24.000001', '1234',  '8'])  # list of mock inputs here
    def test_get_hours_for_day_range_decimal_greater_than_24(self, mock_input):
        hours = timesheets.get_hours_for_day('Monday')  # testing the input is checking correctly housrs entered.
        self.assertEqual(8, hours)  
    

    @patch('builtins.print')  # builtins ? 
    def test_display_total(self, mock_print):
        timesheets.display_total(123)
        mock_print.assert_called_once_with('Total hours worked: 123')  # testing the print function display


    @patch('timesheets.alert') 
    def test_alert_meet_min_hours_doesnt_meet(self, mock_alert):
        timesheets.alert_not_meet_min_hours(12, 30)  
        mock_alert.assert_called_once()  # testing now that the aleart is called once. is alerting


    @patch('timesheets.alert') 
    def test_alert_meet_min_hours_does_meet(self, mock_alert):
        timesheets.alert_not_meet_min_hours(40, 30)  
        mock_alert.assert_not_called()  # testing now that the aleart is not called, not alerting.   

    @patch('timesheets.get_hours_for_day')
    def test_get_hours(self, mock_get_hours):       
        mock_hours = [5, 7, 9]  # list of mock hours, example 
        mock_get_hours.side_effect = mock_hours  # will help make assertions with example data
        days = ['g', 'x', 'k']  # variable days data is fake data like a placeholder
        expected_hours = dict(zip(days, mock_hours))  # expected output: dict funct and zip funct creates a dictionary of {'m': 5, 't': 7, 'w': 9}
        hours = timesheets.get_hours(days)  # days arguments is use to give data to hours  
        self.assertEqual(expected_hours, hours)  # test checking arguments 


    @patch('builtins.print')
    def test_display_hours(self, mock_print):
        #arrange
        example = {'M': 3, 'T': 12, 'W': 8.5}  
        expected_table_calls = [
            call('Day            Hours Worked   '),
            call('M              3              '),  # 15 spaces like the function in timesheets.
            call('T              12             '),
            call('W              8.5            '),
        ]    # tuple of data makes up a mock chart
        # action
        timesheets.display_hours(example)  #call to example for data
        mock_print.assert_has_calls(expected_table_calls)  # function call to ptint table or chart.

       
    def test_total_hours(self):
        example = {'M': 3, 'T': 12, 'W': 8.5} 
        total = timesheets.total_hours(example)
        expected_total = 3 + 12 +8.5  # hours in example should be expeceted.  
        self.assertEqual(total, expected_total)

if __name__ == '__main__':
    unittest.main()        

