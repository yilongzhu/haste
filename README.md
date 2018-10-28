# Haste - A Peer-to-Peer Grocery Delivery App
Yilong Zhu ([@yilongzhu](https://github.com/yilongzhu "Allen's GitHub"))

Daniel Kong ([@danielkong365](https://github.com/danielkong365 "Daniel's GitHub"))


## HackATL 2018 Project
### Motvation
For our submission in the Social Innovation category, we built an peer-to-peer grocery shopping application called Haste. Haste revolves around two user groups: university students that need groceries and people already at the grocery store. Many students have no reliable access to transportation or may be short on time and cannot go to grocery store. With Haste, they are able to place a request for groceries.

People already at the grocery store can open Haste and see a feed of grocery store orders. Shoppers can accept a request and pick up the items listed. After delivery, they can complete their task then have money credited to their account!

### Flaws
Security definitely needs to be upped: users can easily manipulate the app in the state is is in. Also, to process payments we would have to use a third-party API, driving up our variable costs. Our model relies on having university students at the grocery stores that are willing to deliver.


## Installation
1. Clone the repository
2. Create a Python virtual environment with `python3 -m venv venv`
3. Install Python dependencies with `pip install -r requirements.txt`
4. Run the app in developement with `flask run`
5. Run the app in production with the server of your choice!


## Technologies Used
* **Flask** to build the app
* **Flask-SQLAlchemy** as our ORM
* **Flask-Migrate** for database migration
* **Flask-Login** for user accounts
* **Flask-WTF** to make our forms
* **Flask-** to make our forms
* **Bootstrap 4** for front-end design
