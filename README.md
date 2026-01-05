# APP_NAME = VNRealm

Setting things up:

-clone repository

-Open the project in your preferred IDE

virtual configurations:

-Install any dependencies

pip install -r requirements.txt

copy the given env example file and rename it as env, then give it a secret key of your own
-then run this command
	
# Linux / Mac
python3 -m venv venv
source venv/bin/activate

# Windows
python -m venv venv
venv\Scripts\activate


run migrations:
 -python manage.py migrate

Create a superuser ,needed to access the admin site:
    python manage.py createsuperuser

-vn records can be loaded
After running migrations, load this in terminal:

    python manage.py loaddata all_data.json


-apply command in terminal --> python manage.py runserver


Using the website:

A website that displays Visual Novel records with their respective attributes. As a user enters the website, a bunch of visual novels are displayed. 
-The user can click on the title of their desired visual novel to view reviews done by other users. 

-Current user can try to post their own review, but they would be prompted to log in/sign up first.

-User can sign up by setting their own username and password.

-After logging in or setting up an account, users can resume looking at the VN they were previously looking at or go to the homepage and set up their profile.

-In their profile, they can upload their profile picture by choosing a file, then clicking update, and look at the date they created the account. To delete the profile picture user must click on update, check the image in the clear checkbox, and click update again.

-The user can select VN's by clicking add on the list from the dropdown to add them to their played_list, and later can score them and save them, and delete them later on if they want.

-The user can also toggle the visibility switch, which controls adult VN's from appearing in the index page. If they check the option, adult VN's would become visible in the index page.

-In the VN_detail page that comes after clicking the visual novel title on the main page, reviews done by other users are visible with the username and the date posted. The current user, after submitting their review, is able to erase their own review by clicking delete.

-Current user can logout from the home page.

