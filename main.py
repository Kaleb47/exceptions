#Exception handler: code that responds when exceptions are raised and prevents program from crashing.

#try:
#statements
 #   except exceptionName:
#statements


def main():
    try:
        # Get the number of hours worked.
        hours = int(input('How many hours did you work? '))
        # Get the hourly pay rate.
        pay_rate = float(input('Enter your hourly pay rate: '))
        # Calculate the gross pay.
        gross_pay = hours * pay_rate
        # Display the gross pay.
        print('Gross pay: $', format(gross_pay, ',.2f'), sep='')
    except ValueError as err:
        print(err)
# Call the main function.
main()


# try/except statement may include an optional else clause, which appears after all the except clause