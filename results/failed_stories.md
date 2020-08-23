## interactive_story_1
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* get_location
    - slot{"location": "Bangalore"}
    - action_check_service_availability
    - utter_ask_cuisine
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - utter_ask_budget
* budget{"price": "<300"}
    - slot{"price": "<300"}
    - slot{"price": "<300"}
    - utter_confirm_inputs
* affirm
    - action_search_restaurants
    - utter_ask_email_topten
* affirm
    - utter_ask_email_id
* give_emailid{"email_id": "himadri.hk@gmail.com"}
    - slot{"email_id": "himadri.hk@gmail.com"}
    - slot{"email_id": "himadri.hk@gmail.com"}
    - action_send_email_topten
    - utter_goodbye
    - action_restart   <!-- predicted: action_listen -->


## interactive_story_1
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "Bangalore"}
    - slot{"location": "Bangalore"}
    - slot{"location": "Bangalore"}
    - action_check_service_availability
    - utter_ask_cuisine
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - utter_ask_budget
* budget{"price": "<300"}
    - slot{"price": "<300"}
    - slot{"price": "<300"}
    - utter_confirm_inputs
* affirm
    - action_search_restaurants
    - utter_ask_email_topten
* affirm
    - utter_ask_email_id
* give_emailid{"email_id": "himadri.hk@gmail.com"}
    - slot{"email_id": "himadri.hk@gmail.com"}
    - slot{"email_id": "himadri.hk@gmail.com"}
    - action_send_email_topten
    - utter_goodbye
    - action_restart   <!-- predicted: action_listen -->


## interactive_story_1
* greet
    - utter_greet
* restaurant_search{"location": "swarg"}
    - slot{"location": "swarg"}
    - slot{"location": "swarg"}
    - action_check_service_availability
    - utter_goodbye   <!-- predicted: utter_ask_cuisine -->


