from fastapi import FastAPI
from reactpy.backend.fastapi import configure
from reactpy import component, event, html, use_state
import reactpy as rp
from fastapi.middleware.cors import CORSMiddleware
from pymongo import MongoClient
from pymongo.server_api import ServerApi

#connecting to fastapi to connect the webpage with MongoDB database
app=FastAPI()

@component
def Signup_credential():
    ## Creating state
    alltodo = use_state([])
    first_name, set_first_name = use_state("")
    Last_name,set_Last_name=use_state("")
    E_mail,set_E_mail=use_state("")
    phone_number,set_phone_number=use_state("")
    password, set_password = use_state("")
    gender,set_gender=use_state("")



    def submit(event):
        newtodo = {"first_name": first_name,"Last_name":Last_name,"E_mail":E_mail,"phone_number":phone_number,"gender":gender,"password": password}

        # push this to alltodo
        alltodo.set_value(alltodo.value + [newtodo])
        login(newtodo)  

    



    list = []
    def handle_event(event):
        print(event)
        
        
    #UI/UX design code of the webpage using html and css
    return html.div(
      {"style": 
         {  "padding": "50px",
            "display": "flex",
            "align-items": "center",
            "justify-content": "center",
            "background_image":"url(https://mitz77.neocities.org/reactpy/wallpaperflare.com_wallpaper.jpg)", 
            "background-size":"cover",
            "margin": "0px",
            "min-height": "600px",
            "min-width":"600px",
           }
           },

        # creating form to get sign up credentials
        html.form(
        
               {"on submit": submit},
                html.b(html.h1(
                    {"style": {"font-family": "Arial", "font-size": "40px","color":"LightCyan"}}
                    ,"Webpage Signup Form",)),
                html.br(),

                    html.b(html.h2(
                    {"style": {"font-family": "Arial", "font-size": "30px","color":"LightCyan"}}
                    ,'Fill in the below details to Sign up')),

                html.label(
                    {"style": {"font-family": "Arial", "font-size": "25px","color":"#e6fffa"}}
                    ,"First name"),
                html.br(),
                html.input(
                    {
                        "type": "test",
                        "placeholder": "Enter First name",
                        "on_change": lambda event: set_first_name(event["target"]["value"]),
                          "style": {
                             "font-family": "Arial",
                             "font-size": "20px",
                             "padding": "10px 15px",
                            "border": "1px solid #ccc",
                            "border-radius": "20px",
                            "margin": "10px auto",
                            "width": "100%",
                            "box-sizing": "border-box",
                            "background-color": "#FFE4E1",
                            "color": "#555",
                            "outline": "none",
                            },
                        
                    }
                    ),
                html.br(),

                html.label(
                    {"style": {"font-family": "Arial", "font-size": "25px","color":"#e6fffa"}}
                    ,"Last name"),
                html.br(),
                html.input(
                    {
                        "type": "test",
                        "placeholder": "Enter Last name",
                        "on_change": lambda event: set_Last_name(event["target"]["value"]),
                        "style": {
                             "font-family": "Arial",
                             "font-size": "20px",
                             "padding": "10px 15px",
                            "border": "1px solid #ccc",
                            "border-radius": "20px",
                            "margin": "10px auto",
                            "width": "100%",
                            "box-sizing": "border-box",
                            "background-color": "#FFE4E1",
                            "color": "#555",
                            "outline": "none",
                            },
                    }
                ),

                html.br(),
                html.p(""),
                html.label(
                    {"style": {"font-family": "Arial", "font-size": "25px","color":"#e6fffa"}}
                    ,"E-Mail"),
                html.br(),
                html.input(
                    {
                        "type": "test",
                        "placeholder": "Enter Email",
                        "on_change": lambda event: set_E_mail(event["target"]["value"]),
                        "style": {
                             "font-family": "Arial",
                             "font-size": "20px",
                             "padding": "10px 15px",
                            "border": "1px solid #ccc",
                            "border-radius": "20px",
                            "margin": "10px auto",
                            "width": "100%",
                            "box-sizing": "border-box",
                            "background-color": "#FFE4E1",
                            "color": "#555",
                            "outline": "none",
                            },
                    }
                    ),

                html.br(),
                html.p(""),
                html.label(
                    {"style": {"font-family": "Arial", "font-size": "25px","color":"#e6fffa"}}
                    ,"phone number"),
                html.br(),
                html.input(
                    {
                        "type": "test",
                        "placeholder": "Enter Phone number",
                        "on_change": lambda event: set_phone_number(event["target"]["value"]),
                        "style": {
                             "font-family": "Arial",
                             "font-size": "20px",
                             "padding": "10px 15px",
                            "border": "1px solid #ccc",
                            "border-radius": "20px",
                            "margin": "10px auto",
                            "width": "100%",
                            "box-sizing": "border-box",
                            "background-color": "#FFE4E1",
                            "color": "#555",
                            "outline": "none",
                            },
                    }
                ),

                html.br(),
                html.p(""),
                html.label(
                    {"style": {"font-family": "Arial", "font-size": "25px","color":"#e6fffa"}}
                    ,"Gender"),
                html.br(),
                html.select(
                    {  
                        "on_change": lambda event: set_gender(event["target"]["value"]),
                        "style":{
                             "font-family": "Arial",
                             "font-size": "20px",
                             "padding": "10px 15px",
                            "border": "2px solid #ccc",
                            "border-radius": "20px",
                            "margin": "10px auto",
                            "width": "100%",
                            "background-color": "#FFE4E1",
                            "color": "#555",
                            "outline": "none"}
                        

                    },
                    html.option(
                    {
                        "value":"Male",
                        "style":{
                             "font-family": "Arial",
                             "font-size": "20px",
                             "padding": "10px 15px",
                            "border": "2px solid #ccc",
                            "border-radius": "10px",
                            "margin": "10px auto",
                            "width": "100%",
                            "box-sizing": "border-box",
                            "background-color": "#FFE4E1",
                            "color": "black",
                            "outline": "none"}
                    },"Male"),
                    html.option(
                    {
                        "value":"Female",
                        "style":{
                             "font-family": "Arial",
                             "font-size": "20px",
                             "padding": "10px 15px",
                            "border": "2px solid #ccc",
                            "border-radius": "10px",
                            "margin": "10px auto",
                            "width": "100%",
                            "box-sizing": "border-box",
                            "background-color": "#FFE4E1",
                            "color": "black",
                            "outline": "none"}
                    },"Female")
                ),
                html.br(),
                html.p(""),
                html.label(
                    {"style": {"font-family": "Arial", "font-size": "25px","color":"#e6fffa"}}
                    ,"Password"),
                html.br(),
                html.input(
                    {
                        "type": "password",
                        "placeholder": "Enter Password",
                        "on_change": lambda event: set_password(event["target"]["value"]),
                        "style": {
                             "font-family": "Arial",
                             "font-size": "20px",
                             "padding": "10px 15px",
                            "border": "1px solid #ccc",
                            "border-radius": "20px",
                            "margin": "10px auto",
                            "width": "100%",
                            "box-sizing": "border-box",
                            "background-color": "#FFE4E1",
                            "color": "#555",
                            "outline": "none",
                            },
                    }
                ),
                
                html.br(),
                html.p(""),
                # creating submit button on form
                html.button(
                    {
                        "type": "Create an Account",
                        "on_click":event(lambda event:submit(event)),
                        "style": {
                             "font-family": "Arial",
                             "font-size": "20px",
                             "padding": "10px 15px",
                            "border": "1px solid #ccc",
                            "border-radius": "20px",
                            "margin": "10px auto",
                            "width": "100%",
                            "box-sizing": "border-box",
                            "background-color": "#66147a",
                            "color": "#f4f5f0",
                            "outline": "none",
                            },
                    },
                    "Create Account",
                ),
                html.button(
                {
                    "type": "Clear",
                    "on_click":lambda event: set_first_name("") and set_Last_name("") and set_E_mail("") and set_phone_number("") and set_password(0),
                    "style": {
                             "font-family": "Arial",
                             "font-size": "20px",
                             "padding": "10px 15px",
                            "border": "1px solid #ccc",
                            "border-radius": "20px",
                            "margin": "10px auto",
                            "width": "100%",
                            "box-sizing": "border-box",
                            "background-color": "#66147a",
                            "color": "#f4f5f0",
                            "outline": "none",
                            },
                },
                "Clear ALL",
                ),
                ),
        html.ul(list),  
       
    )

#Connection code to open up a connection in MongoDB Atlas colud data base
uri = "mongodb+srv://admin:123@cluster0.d2nrwcm.mongodb.net/"
client = MongoClient(uri, server_api=ServerApi("1"))

##The database name and collection credentials will be stored in
db = client["NoSQ_webapplication"]
collection = db["Signup_credentials"]

##checking for the data base connectivity 
try:
    client.admin.command("ping")
    print("Sucessfully connected Mongodb")
except Exception as e:
    print(e)


#code to store entered user data from webapplication to MongoDB atlas cloud database
def login(
    login_data: dict,
):  
    first_name= login_data["first_name"]
    Last_name=login_data["Last_name"]
    E_mail=login_data["E_mail"]
    phone_number=login_data["phone_number"]
    password = login_data["password"]
    gender=login_data["gender"]

    ## Creating a document to insert into the collection
    Sen_info={"first_name": first_name,"Last_name":Last_name,"Phone_number":phone_number,"gender":gender}
    ## creating a document within a document to optimization purpose
    document = {"E_mail":E_mail,"sensitive_information":Sen_info,"password": password}
    # logger.info('sample log message')
    print(document)

    ## Insert the document into the collection
    post_id = collection.insert_one(document).inserted_id  # insert document
    print(post_id)

    return {"message": "Login successful"}

configure(app, Signup_credential)

