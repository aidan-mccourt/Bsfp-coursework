----Background----  

This is a web app which is a shop that allows users to register, login and order milkshakes.  
The milkshake ordering process has users select which ice-cream, flavour and topping they want before ordering it.


----required----  

You will need:  
Python v 3.10.0 or higher  
Django 2.2.24  
pytz 2021.3  
sqlparse 0.4.2  
coverage 6.2   
You will also need a virtual enviroment to run the server   


----Admin details----   
Once the app is running you can access the admin page with /admin added onto url    
The username : admin     
Password : admin    
Through the admin page you can edit and add new entries to the ice_cream, flavour and toppings tables.    
You are also able to edit and add to the User and milke_shake tables as well if you need to.    


----project file location details----    
The shop section of the repository contains the main webpages, models(database tables) and tests    
The user section contains the register form for usres and logining in    
The html for each web page is located in templates and the css is located in static    


----to run the server----     
once you have navigated into the directory and are in your virtual enviroment run:    
manage.py runserver    


Migrations is the logs of all prevoius migrations to the system. To edit the database tables you will need to create a migration and then migrate it.    
The commands:    
manage.py makemigrations make_a_shake   
Then:    
manage.py migrate     
    


