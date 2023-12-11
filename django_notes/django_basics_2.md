### Server Side Rendering (SSR) and client Side Rendering (CSR)
- In SSR, the server itself creates an HTML page and loads the data into it and sends it to client only to display.
- Initial page loading is faster and SEO will be better in SSR.
- In CSR, server sends data to client and client renders the user interface using the data.
- Apps are more interactive. CSR is now used everywhere, where server side developer shares API to frontend developers.

### Few points when developing SSR
- We will have to create a template folder inside app that keeps html files.
- Folder structure should be template/app_name/html_file.html (notice here the app_name folder inside template directory).
- This keeps away conflit among multiple templates present as projects grow bigger.
- Just like template, we keep static files inside static folder inside an app, static/app_name/css/style.css.
- We run command "python manage.py collectstatic" to move all the static assets from all the apps to 'staticfiles' location.
- This command keeps all the assets from all the apps to a single location ('staticfiles').
- To run the above command we need to specify 'staticfiles' location in settings.py script of the project. (STATIC_ROOT = BASE_DIR / 'staticfiles')
- This is helpful when we run our server in production environment, it uses this location.
- Also, it helps in caching, let's say any static content is changed on the server, when we run the above command, it gets reflected in the 'staticfiles', and this new version of the file has some change that is noticed by the client, which then updates the cache to render this new content.


### Creating form on Django (Post request):
- We create a forms.py file in our app dirctory.
- We use ModelForm class for creating form inside forms.py.
- Inside html, inside form tag, we use 'action' (here we set which url is called when the form is submitted) and we use 'method' ('POST', 'GET' etc.).
### CSRC token (Cross-site Request Forgery)
- We use "{% csrf_token %}" inside form tag.
- CSRF - Cross-Site Request Forgery, When a user is already authenticated on a website, he won't be asked again to login if he comes back to the website.
- An attacker may send a tempting link via email or sms to the user, that will allow user to submit information to the website without them knowing (and since the user is already logged in).
- This may lead to unintended actions being performed on user's behalf (unauthorized trasaction, data updation, deletion etc.).
- To help prevent this, server keeps csrf token for a session and when any form is submitted this token is also send in the request.
- This token is then matched with existing token on the server, if matched then only server makes the submission valid otherwise rejects.

### Miscelleneous
- python manage.py migrate your_app_name zero
- Above line unapplies all the migration.
