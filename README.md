# REST-API-Task

It provides the following services

1. Given a bank branch IFSC code, get branch details
2. Given a bank name and city, get details of all branches of the bank in the city

# Working

The app is deployed in Heroku. URL: https://degrassi-parliament-06647.herokuapp.com/

1. To get branch details for a given IFSC CODE, make a GET request to https://degrassi-parliament-06647.herokuapp.com/branch/[IFSC CODE]. 

    EG:https://degrassi-parliament-06647.herokuapp.com/branch/ABHY0065009/
    
    ![alt text](Result1.jpg?raw=true)
    

2. To get details of all branches of the bank in the city, make a POST request to https://degrassi-parliament-06647.herokuapp.com/all with parameters name and city.
    
    ![alt text](result2.jpg?raw=true)
