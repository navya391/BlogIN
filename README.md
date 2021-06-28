BlogIN

Full Featured Blogging Web App
   

This Blogging web application project is purely made with Django as the backend and Bootstrap as the frontend.

Clone This Project (Make Sure You Have Git Installed)
https://github.com/navya391/BlogIN.git

Install Dependencies

pip install -r requirements.txt
Set Database 

python manage.py makemigrations
python manage.py migrate

Create SuperUser
python manage.py createsuperuser

After all these steps , you can start developing this project.

FEATURES

Blog list View:
List all blog posts with Title, category, Author Name, Date Posted, Image.

Latest Posts :
List all the post which are created recently with Image  and Title.

category list :
List all the categories related to the posts

Search :
List all blog posts with the search query that you enter.

Pagination :
To limit with a certain number of posts in each page.

Blog Detail View :
To view the complete blog post when clicked on Read More 

User Authentication :
Login/Register
Users can Login/Register to the Blog App.

Comment :
Users can comment to any blog post after login

Create Blog Post :
Users can create blog posts from the front end 

Edit Profile :
Users can edit Profile Image, cover,about.

Tech Stacks
Language: Python
Framework: Django , Bootstrap

