## complete path
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* get_location OR restaurant_search{"location": "delhi"}
    - slot{"location": "delhi"}
	- action_check_service_availability
    - utter_ask_cuisine
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
	- utter_ask_budget
* budget{"price": "<300"}
	- slot{"price": "<300"}
	- utter_confirm_inputs
> check_all_inputs_received

## affirmative
> check_all_inputs_received
* affirm
    - action_search_restaurants
	- utter_ask_email_topten
* affirm+give_emailid
    - slot{"email_id": "himadri.hk@live.com"}
	- action_send_email_topten
    - utter_goodbye
    - export

## denial
> check_all_inputs_received
* deny
	- utter_goodbye

## interactive_story_1
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
*  get_location OR restaurant_search{"location": "Bangalore"}
    - slot{"location": "Bangalore"}
    - action_check_service_availability
    - utter_ask_cuisine
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - utter_ask_budget
* budget{"price": "300-700"}
    - slot{"price": "300-700"}
    - utter_confirm_inputs
* affirm
    - action_search_restaurants
    - slot{"location": "Bangalore"}
    - utter_ask_email_topten
* affirm
    - utter_ask_email_id
* give_emailid{"email_id": "burnwal.amardeep@gmail.com"}
    - slot{"email_id": "burnwal.amardeep@gmail.com"}
    - action_send_email_topten
    - utter_goodbye

## interactive_story_1
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
*  get_location OR restaurant_search{"location": "Bangalore"}
    - slot{"location": "Bangalore"}
    - action_check_service_availability
    - utter_ask_cuisine
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - utter_ask_budget
* budget{"price": "<300"}
    - slot{"price": "<300"}
    - utter_confirm_inputs
* affirm
    - action_search_restaurants
    - utter_ask_email_topten
* affirm
    - utter_ask_email_id
* give_emailid{"email_id": "himadri.hk@gmail.com"}
    - slot{"email_id": "himadri.hk@gmail.com"}
    - action_send_email_topten
    - utter_goodbye
    - action_restart

## interactive_story_1
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* get_location{"location": "kolkata"}
    - slot{"location": "kolkata"}
    - action_check_service_availability
    - utter_ask_cuisine
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - utter_ask_budget
* budget{"price": "300-700"}
    - slot{"price": "300-700"}
    - utter_confirm_inputs
* affirm
    - action_search_restaurants
    - utter_ask_email_topten
* affirm
    - utter_ask_email_id
* give_emailid{"email_id": "burnwal.amardeep@gmail.com"}
    - slot{"email_id": "burnwal.amardeep@gmail.com"}
    - action_send_email_topten
    - utter_goodbye

## interactive_story_1
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* get_location{"location": "kolkata"}
    - slot{"location": "kolkata"}
    - action_check_service_availability
    - utter_ask_cuisine
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - utter_ask_budget
* budget{"price": "300-700"}
    - slot{"price": "300-700"}
    - utter_confirm_inputs
* affirm
    - action_search_restaurants
    - utter_ask_email_topten
* give_emailid{"email_id": "himadri.hk@live.com"}
    - slot{"email_id": "himadri.hk@live.com"}
    - action_send_email_topten
    - utter_goodbye

## interactive_story_1
* greet
    - utter_greet
* restaurant_search{"location": "Bhopal"}
    - slot{"location": "Bhopal"}
    - action_check_service_availability
    - utter_ask_cuisine

## interactive_story_2
* greet
    - utter_greet
* restaurant_search{"location": "bhopal"}
    - slot{"location": "bhopal"}
    - action_check_service_availability
    - utter_ask_cuisine
* restaurant_search{"cuisine": "North Indian"}
    - slot{"cuisine": "North Indian"}
    - utter_ask_budget
* budget{"price": "300-700"}
    - slot{"price": "300-700"}
    - utter_confirm_inputs
* affirm
    - action_search_restaurants
    - utter_ask_email_topten
* affirm
    - utter_ask_email_id
* give_emailid{"email_id": "burnwal.amardeep@gmail.com"}
    - slot{"email_id": "burnwal.amardeep@gmail.com"}
    - action_send_email_topten
    - utter_goodbye

## interactive_story_1
* greet
    - utter_greet
* restaurant_search{"location": "asansol"}
    - slot{"location": "asansol"}
    - action_check_service_availability
    - utter_ask_cuisine
* restaurant_search{"cuisine": "North Indian"}
    - slot{"cuisine": "North Indian"}
    - utter_ask_budget
* budget{"price": ">700"}
    - slot{"price": ">700"}
    - utter_confirm_inputs
* affirm
    - action_search_restaurants
    - utter_ask_email_topten
* deny
    - utter_goodbye

## interactive_story_1
* greet
    - utter_greet
* restaurant_search{"location": "asansol"}
    - slot{"location": "asansol"}
    - action_check_service_availability
    - utter_ask_cuisine
* restaurant_search{"cuisine": "North Indian"}
    - slot{"cuisine": "North Indian"}
    - utter_ask_budget
* budget{"price": "300-700"}
    - slot{"price": "300-700"}
    - utter_confirm_inputs
* affirm
    - action_search_restaurants
    - utter_ask_email_topten
* deny
    - utter_goodbye

## interactive_story_1
* greet
    - utter_greet
* restaurant_search{"location": "swarg"}
    - slot{"location": "swarg"}
    - action_check_service_availability
    - utter_goodbye

## interactive_story_1
* greet
    - utter_greet
* restaurant_search{"cuisine": "north indian", "location": "ranchi"}
    - slot{"cuisine": "north indian"}
    - slot{"location": "ranchi"}
    - action_check_service_availability
    - utter_ask_budget
* budget{"price": "300-700"}
    - slot{"price": "300-700"}
    - utter_confirm_inputs
* affirm
    - action_search_restaurants
    - utter_ask_email_topten
* deny
    - utter_goodbye

## interactive_story_1
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* get_location{"location": "bangalore"}
    - slot{"location": "bangalore"}
    - action_check_service_availability
    - utter_ask_cuisine
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - utter_ask_budget
* budget{"price": "300-700"}
    - slot{"price": "300-700"}
    - utter_confirm_inputs
* affirm
    - action_search_restaurants
    - utter_ask_email_topten
* affirm
    - utter_ask_email_id
* give_emailid{"email_id": "himadri.hk@gmail.com"}
    - slot{"email_id": "himadri.hk@gmail.com"}
    - action_send_email_topten
    - utter_goodbye
