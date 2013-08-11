# this is a python class that hackily scrapes
# all the data of the person.

# what data are we interested in?

class UP_Scraper(object):
  
  def __init__(upconnect, token, user_id):
      self._upconnect = upconnect
      self._token = token
      self._user_id = user_id

  def meals():
      meals = _upconnect.get_meals(_token)
      # parse meals data into a database model
      # time of day, number of calories, type
      for meal in meals['data']['items']:
        is_caffeine(meal)
        is_alcohol(meal)
      

  def is_caffeine(meal):
      title = str(meal['title']).lowercase
      caffeinated = ['cappucino', 'soda', 'cola', 'tea', 'coffee', 'chocolate'] 
      


  def is_alcohol(meal):
      if str(meal['title']).lowercase in ['beer', 'wine', 'cocktail', 'bourbon', 'whiskey', 'margarita']
      
      
  def workouts():
      workouts = _upconnect.get_meals(_token)
       

  def sleep():
      sleeps = _upconnect.get_sleeps(_token)
      for sleep in sleeps['data']['items']:
      # log sleep items to the database
          date = sleep['date']
          for detail, value in sleep['details']
              fact = DayFacts.objects.create(date=date, feature=detail, value=value)
              fact.save()
