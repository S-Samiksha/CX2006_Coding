# READ THIS!!!!
Bold: Do it<br>
Italics: Check it (dont not check it, please check it. I think we dont have time for everyone to check. So once those two are done means can submit) <br>

## Important Lectures 
Design pattern: week of 11 oct 
Testing 18 oct week lectures 

## Locations of all documents (update there directly)
Code: https://github.com/S-Samiksha/CX2006_Coding/tree/main/Coding <br>
Test and Testcases: https://github.com/S-Samiksha/CX2006_Coding/tree/main/Coding/Testing <br>

SRS document: https://entuedu-my.sharepoint.com/:w:/r/personal/samiksha002_e_ntu_edu_sg/Documents/CX2006/Group%20Project/Final%20SRS.docx?d=w8c13886884a6467c99bdcfac463748c1&csf=1&web=1&e=eEE4rM <br>

<!--UI MOCK UP LINK:  https://docs.google.com/presentation/d/1dIuQCkmmF8AWjBT9cTfn94fV4n_XEfiyTaNp6yWQWBk/edit?usp=sharing
Documentation: https://github.com/S-Samiksha/CX2006_Coding/tree/main/Documentation/lab_3_submission <br> -->

## Deadlines (TO BE CONFIRMED, WE NEED TO ADJUST THIS)
On **Sunday 31 Oct, 9.30pm**, I will download the zip from github and submit with the pdf document. <br>
11 Nov: CX2006 Part 2 Quiz during lecture time <br>
29 Nov: CX2006 finals only part 1 tested <br>

## Weightage
Group Project: 50% <br>
quiz: 25% <br>
finals: 25% <br>


### All the best guys!!! 


---
## Testing (after finishing backend)
Manual table thing for documentation **Arushi** , **Melise** , **Samiksha** (take 3 pages each to make) <br>
flask automated testing for login and logout(for doing autmation purposes just one or two shld be okay): **Samiksha** <br> 

**Manual test (give feedback if anything is not working, test all the buttons, anything that can click must work**

Test Manually: login, logout, recommendation **Marcus** <br>
Test Manually: update roommate, update self **Junhan** <br>
Test Manually: Messages **Anagha** <br>
Test Manually: Search Houses **Samiksha** <br>

**Flow of demo/video**

Register a dummy account --> then just use account 1 from there 

Test accounts to be used: Account 1 and Account 5

Login using Account 1

Update self/roommate: Account 1

Account 1 messages Account 5 (maybe have account 1 saying 'yes lets room tgt!' in the demo, with a prev chat history of them discussing **marcus** decide)

Test accounts to use 'skip' button in recommendation: Account 2

Search House (One locations, **Junhan** choose):

Logout successfully back to main page 



## Backend 

#### Stuff that needs to be standardized
1. If you install some libraries frameworks etc. put it into the requirements.txt(e.g. pandas, sql, flask, without pandas the home page wont show which means nth will work)
2. To download all the requirements, go into the folder with the requirements.txt in cmd line / terminal. Run (`pip install -r requirement.txt`) --> do this everytime so if anyone made edits flask can run on your laptop
3. All the python stuff is to be added into auth.py --> all routes are made and comments are made for sql commands taken from online (tech with tim, w3 schools) when you go in read the thing at the top
4. about page and main page is in views.py 
5. do not touch __init__.py and main.py 
6. run main.py to run flask application (in VS code ctr + shift + N) fire up local host 

**Do we want a virtual environment?** 

Compile into one executable app.py file + readme guidelines + set up env: **Samiksha** <br>
Make the database for the landlord emails: **Marcus** <br>
Make the CSV for the roommate preference (remember they are different databases in the Use Case):  Done 
Request to API (gov.sg): **Junhan** <br>
Registration,login,logout: **Anagha**  <br>
update profile, update roommate profile: **Anagha**  <br>
Messages: **Marcus**  <br>
Rommmate recommendation + home page: **Samiksha**  <br>
Search House: **Junhan**  <br>
video screen recording: **Samiksha** <br>

---

## Documentation
**Arushi** **Melise**
1. Make sure ALL diagrams are coherent when reading, meaning the functions and class diagrams and the use case diagram, use case all match match (ensure it accommodates the stuff the TA said)  update according to the pdf
remember to remove tenant email 

> UC001 to UC004 (table and sequence): 
> UC005 to UC0010 (table and sequence): 
> Intial Dialog:
> UML: 

--

All the new stuff
also finalize within your own "micro" group if everyone (all 6 people) checks we will take forever. 

2. New class diagram   (One take Control, one take entity, one take boundary respectively once the first person is done, just update to github and pass on) --> many to one, one to one etc. 

3. Make the system architecture 

4. Make the state machine (take intial dialog convert to even more boring form)

5. Make the communication diagram  (Split 50/50, iirc each sequence diagram got one communication)

6. Make the activity diagram  (take state machine to even more boring form its the same and yet just more boring)

7. Do video scripting  (cuz need to screen record)

8. Do the video 

9. Data dictionary finalize   (split 50/50)

10. UI mockup compile the final one and explain based on the use case.  (split 50/50)

11. font size, font type, alignment etc. 

12. Whoever wanna nit grit on the design and the website and critique how the website works: 

---



## References:

1. Codes were adapted from for home.html: w3schools (2021) https://www.w3schools.com/howto/howto_js_slideshow.asp retrieved 3 oct 2021
2. Codes were adapted from for home.html: w3schools (2021) https://www.w3schools.com/howto/howto_js_slideshow.asp retrieved 3 oct 2021
3. Codes were adapted from for home.html: w3schools (2021) https://www.w3schools.com/howto/howto_js_slideshow_gallery.asp retrieved 3 oct 2021
4. Codes were dapted from for home.html: w3schools (2021) https://www.w3schools.com/howto/ retrieved 3 oct 2021
5. Codes were taken and adapted from for all pages: https://github.com/WebCifar/one-page-website-html-css-project-for-practice 
6. https://www.free-css.com/free-css-templates/page270/felicity 
7. Reference taken from: https://www.digitalocean.com/community/tutorials/css-cropping-images-object-fit retrieved 9 oct 2021




## Front-end (DONE)

*main folder* <br>

1. Main Page: main.html **Samiksha** 
2. About Page: about.html **Marcus** 

- These are static no need to worry


*register_login folder* <br>

3. Registration Page: register.html **Anagha** 
4. Login Page: login.html **Arushi** 

- Make sure password cannot be seen when typing in 
- if needed, do the encryption 

*home_page folder*

5. Home Page: home.html **Samiksha** (done)
- Recommendation Lowkey AI thing 
- Logout Function

*view_update_profile* <br>

6. View Profile: profile.html **Melise** 
7. Update roommate profile page: update_roommate.html **Arushi**
8. Update self profile page: update_self.html **Anagha** 

- form validation 


*search_view_houses* <br>

9. Search House page: search_house.html **Melise** 
10. view result of house page: view_houses.html **junhan** 
- Update the sql database, change it **might have to work together** 

*Messages*

11. Chat Box Page **Marcus** : messages.html
- this difficult one

*tenant_email*

12. Tenant Email Landlord **Junhan**: tenant_email.html
- form validation 



