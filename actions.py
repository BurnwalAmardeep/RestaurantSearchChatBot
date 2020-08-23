from rasa_sdk import Action
from rasa_sdk.events import SlotSet
import zomatopy
import json
from string import Template

import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from threading import Thread

class ActionSearchRestaurants(Action):

    def name(self):
        return 'action_search_restaurants'
	
    def filter_by_price(self,tracker, price):
        #price = restaurant['restaurant']['average_cost_for_two']
        selected_price=tracker.get_slot('price')
        if(selected_price =="<300"):
            return (price <= 300)
        if(selected_price =="300-700"):
            return ((price > 300) & ( price <=700))
        if(selected_price ==">700"):
            return (price > 700)
        
    
    def run(self, dispatcher, tracker, domain):
        config={ "user_key":"b56f808eeca06454bf8c0b3e2186e70f"}
        zomato = zomatopy.initialize_app(config)
        loc = tracker.get_slot('location')
        cuisine = tracker.get_slot('cuisine')
        location_detail=zomato.get_location(loc, 1)
        d1 = json.loads(location_detail)
        lat=d1["location_suggestions"][0]["latitude"]
        lon=d1["location_suggestions"][0]["longitude"]
        cuisines_dict={'bakery':5,'chinese':25,'cafe':30,'italian':55,'biryani':7,'north indian':50,'south indian':85}
        results=zomato.restaurant_search("", lat, lon, str(cuisines_dict.get(cuisine)), 30)
        d = json.loads(results)
        response=""
        #d=list(filter(self.filter_by_price, d['restaurants']))
        
        filtered_res = []
        for rest in d['restaurants']:
            price_for_two=rest['restaurant']['average_cost_for_two']
            #print(price_for_two)
            res = self.filter_by_price(tracker, price_for_two)
            if (res):
                #print('success rest ' + rest)
                filtered_res.append(rest)
            #d['restaurants']=filtered_res
        
        filtered_res.sort(key=lambda x : x['restaurant']['user_rating']['aggregate_rating'], reverse=True)
        
        if d['results_found'] == 0:
            response= "no results"
        else:
            response="Found \n"
            ctr=1
            for restaurant in filtered_res[0:5]:
                response=response+ str(ctr)+"). "+restaurant['restaurant']['name']+ " in "+ restaurant['restaurant']['location']['address']+ " has been rated "+ restaurant['restaurant']['user_rating']['aggregate_rating']+"\n"
                ctr+=1
        
        #print(str(filtered_res))
        dispatcher.utter_message("\n-----------------------------------------------------------\n"+response)
        return

class CheckServiceAvailability(Action):
    def name(self):
        return 'action_check_service_availability'
        
    def run(self,dispatcher,tracker,domain):
        servicing_cities=['ahmedabad','bangalore','chennai','delhi','hyderabad','kolkata','mumbai','pune','agra','ajmer','aligarh','amravati','amritsar','asansol','aurangabad','bareilly','belgaum','bhavnagar','bhiwandi','bhopal','bhubaneswar','bikaner','bilaspur','bokarosteelcity','chandigarh','coimbatore','cuttack','dehradun','dhanbad','bhilai','durgapur','erode','faridabad','firozabad','ghaziabad','gorakhpur','gulbarga','guntur','gwalior','gurgaon','guwahati','hamirpur','hubli–dharwad','indore','jabalpur','jaipur','jalandhar','jammu','jamnagar','jamshedpur','jhansi','jodhpur','kakinada','kannur','kanpur','kochi','kolhapur','kollam','kozhikode','kurnool','ludhiana','lucknow','madurai','malappuram','mathura','goa','mangalore','meerut','moradabad','mysore','nagpur','nanded','nashik','nellore','noida','patna','pondicherry','purulia','prayagraj','raipur','rajkot','rajahmundry','ranchi','rourkela','salem','sangli','shimla','siliguri','solapur','srinagar','surat','thiruvananthapuram','thrissur','tiruchirappalli','tiruppur','ujjain','bijapur','vadodara','varanasi','vasai-virarcity','vijayawada','visakhapatnam','vellore','warangal']
        
        loc=tracker.get_slot('location')
        
        if(loc.lower() not in servicing_cities):
            dispatcher.utter_message("Sorry :( We do not operate in that area yet. ")
        
        return

class EmailService(Action):
   
    def __init__(self):
        self.smtp_host = 'smtp.gmail.com'
        self.smtp_port = 25
        self.team_foodie_email = '<chatbot_email>'
        self.team_foodie_pwd = '<chatbot_email_pwd>'
        self.email_subject = 'List of top 10 restaurants for your hunger'
        self.msg_success = 'Mail sent to the email. Have a good day.'
        self.msg_failure = 'Sorry,  we are unable to send the mail. Please try again in sometime.'
    
    def filter_by_price(self,tracker, price):
        selected_price=tracker.get_slot('price')
        if(selected_price =="<300"):
            return (price <= 300)
        if(selected_price =="300-700"):
            return ((price > 300) & ( price <=700))
        if(selected_price ==">700"):
            return (price > 700)
        
    
    def get_restaurants(self,tracker):
        config={ "user_key":"<your_user_key>"}
        zomato = zomatopy.initialize_app(config)
        loc = tracker.get_slot('location')
        cuisine = tracker.get_slot('cuisine')
        location_detail=zomato.get_location(loc, 1)
        d1 = json.loads(location_detail)
        lat=d1["location_suggestions"][0]["latitude"]
        lon=d1["location_suggestions"][0]["longitude"]
        cuisines_dict={'bakery':5,'chinese':25,'cafe':30,'italian':55,'biryani':7,'north indian':50,'south indian':85}
        results=zomato.restaurant_search("", lat, lon, str(cuisines_dict.get(cuisine)), 15)
        d = json.loads(results)
        response=""
        
        filtered_res = []
        for rest in d['restaurants']:
            price_for_two=rest['restaurant']['average_cost_for_two']
            #print(price_for_two)
            res = self.filter_by_price(tracker, price_for_two)
            if (res):
                #print('success rest ' + rest)
                filtered_res.append(rest)
        
        return filtered_res
        
    def name(self):
        return 'action_send_email_topten'
        
    def run(self,dispatcher,tracker,domain):
        self.cust_email=tracker.get_slot('email_id')
        tmp_restaurants=self.get_restaurants(tracker)
        tmp_restaurants.sort(key=lambda x : x['restaurant']['user_rating']['aggregate_rating'], reverse=True)
        #print(tmp_restaurants)
        return self.send_email(tmp_restaurants)
    
    def set_up_email_server(self):
# set up the SMTP server
        smtp_server = smtplib.SMTP(host= self.smtp_host, port=self.smtp_port)
        smtp_server.starttls()
        smtp_server.login(self.team_foodie_email, self.team_foodie_pwd)
        print('inside set up mail ',self.smtp_host,self.smtp_port,self.team_foodie_email,self.team_foodie_pwd)
        return smtp_server

# In[4]:

    def trigger_email(self, smtp_server, cust_email, message):
        
        
        msg = MIMEMultipart()       # create a message
        
        # setup the parameters of the message
        msg['From']= self.team_foodie_email
        msg['To']= self.cust_email
        msg['Subject']= self.email_subject
        
        # add in the message body
        msg.attach(MIMEText(message, 'plain'))
        
        smtp_server.send_message(msg)
        del msg
        print('inside trigger email')
        smtp_server.quit()
        return

    def prepare_message(self,restaurants):
        rest_template = Template('${idx}). ${restaurant_name} in ${restaurant_address} with avg budget of ${budget} has been rated ${rating}.\n')
        messages = ['Dear Customer, \n\n Here are the top 10 restaurants as per your search. \n \n']
        ctr=1
        for rest in restaurants[0:10]:
            messages.append(rest_template.substitute(idx = ctr,restaurant_name = rest['restaurant']['name'], 
                                                     restaurant_address = rest['restaurant']['location']['address'],budget = rest['restaurant']['average_cost_for_two'], rating = rest['restaurant']['user_rating']['aggregate_rating']))
            ctr+=1
        messages.append('\nKind Regards,\nTeam Foodie')
        final_message = ''.join(messages)
        print('inside prepare message')
        return final_message


    # In[7]:


    def send_email(self,restaurants):

        final_message = self.prepare_message(restaurants)
        ##print(final_message)
        #try:
        smtp_server = self.set_up_email_server()
        #except:
        #    print(msg_failure)
        
        #try:
        thr = Thread(target=self.trigger_email, args=[smtp_server, self.cust_email,final_message])
        thr.start()
        #self.trigger_email(smtp_server, self.cust_email, final_message)
        #except:
        #    print(msg_failure)

        return
        
    