
Registration and Login system using file handling Python

I have designed a basic registration and login system using file handling in Python. 

Initially the user will be asked to enter a choice based on their preference, 1 for registration and 2 for login.

--->If the user enter "1", they will be prompted to enter the new email address and password. 
        Email address will have a pre-defined format defined in def email_validation(ea) such as:
            email should have "@" and followed by "."      
                eg:- sherlock@gmail.com
                nothing@yahoo.in

            email should not be like this 
                eg:- @gmail.com
                there should not be any "." immediate next to "@"
                eg:- my@.in
                it should not start with special characters and numbers
                eg:- 123#@gmail.com

---> Every time the user enters an invalid password, they will be prompted to restart the process. If the email address is succesfully entered, the user will be notified and will proceed to enter the password which will also have the following predefined conditions at def password_validation(pw):
. 
        password (5 < password length > 16)
        Must have minimum one special character,
        one digit,
        one uppercase, 
        one lowercase character 

The user will be asked to enter the password twice for confirmation. If the password entered by the user meets all the conditions specified, then the email address and password details will be saved in a text file named - "database.txt". If the conditions aren't met, the user will be taken over the previous step to restart the process. 


---> If the user enters "2", they will be prompted to enter the email address and password
    The email address will be checked against the existing records in the text file and the user will get a notification.
        If the email address is not found the user will be notified about it and will be asked to register the account.
        If the email adddress is found, the user will be notified and will be further asked to enter the password.
            If the user enter enters the right password, they will be notified as login succesful.
            If the user enters incorrect password, they will be asked to choose the options "1" and "2" to retry or forget password.
                If the user enters "1", then they will have to restart the login process again. 
                If the user enters "2", then they will be asked to be enter the choice "1" and "2" for displaying the password or changing the password respectively. 
                Irrespective of the choice, the user will be asked to enter their email address to verify their identity. 
                If the user enters "1", the password will be displayed. 
                If the user enters "2", they will be asked to enter a new password which will be checked against the conditions specified in def pass_change(ea, new_pass) which will overwrite the existing password in the record. 