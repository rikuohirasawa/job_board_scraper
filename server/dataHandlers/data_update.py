from dotenv import load_dotenv
import os
from pymongo import MongoClient, ReturnDocument
from scraper import scraper

load_dotenv()
MONGO_URI = os.getenv('MONGO_URI')
DB_NAME = os.getenv('DB_NAME')

developer_skills = ['Javascript', 'Python','HTML', 'CSS', 'Python', 'SQL', 'Java', 'Node.js', 'Typescript','c%23', 'Bash', 'c%2B%2B', 'PHP', 'C%20developer', 'PowerShell', 'Golang', 'Kotlin', 'Rust', 'Ruby', 'Dart', 'assembly%20language', 'R%20developer', 'Matlab', 'Groovy', 'Objective-C', 'Scala', 'Perl', 'Haskell', 'Delphi', 'Clojure', 'Elixir', 'LISP', 'Julia', 'F%23', 'Erlang', 'COBOL']

                    # Javascript ,'HTML', 'CSS', 'Python', 'SQL', 'Java', 'Node.js', 'Typescript','c%23', 'Bash', 'c%2B%2B', 'PHP', 'C%20developer', 'PowerShell', 'Golang', 'Kotlin', 'Rust', 'Ruby', 'Dart', 'assembly%20language', 'R%20developer', 'Matlab', 'Groovy', 'Objective-C', 'Scala', 'Perl', 'Haskell', 'Delphi', 'Clojure', 'Elixir', 'LISP', 'Julia', 'F%23', 'Erlang', 'COBOL']

regions = [('AB', '111149'), ('BC', '111152'), ('MB', '111151'), ('NB', '111154'), ('NF', '111157'), ('NT', '111155'), ('NS', '111153'), ('NU', '111148'), ('ON', '111147'), ('PE', '111156'), ('QC', '111158'), ('SK', '111146'), ('YT', '111150')]
          #[('AB', '111149')]   , ('BC', '111152'), ('MB', '111151'), ('NB', '111154'), ('NF', '111157'), ('NT', '111155'), ('NS', '111153'), ('NU', '111148'), ('ON', '111147'), ('PE', '111156'), ('QC', '111158'), ('SK', '111146'), ('YT', '111150')]
            # , ('BC', '111152'), ('MB', '111151'), ('NB', '111154'), ('NF', '111157'), ('NT', '111155'), ('NS', '111153'), ('NU', '111148'), ('ON', '111147'), ('PE', '111156'), ('QC', '111158'), ('SK', '111146'), ('YT', '111150')]

def update_technology_data(date):
    print(date)
    client = MongoClient(MONGO_URI)
    try:
        db = client[DB_NAME]
        technology_collection = db['technology_data']
        region_collection = db['region_data']
        region_list = list(region_collection.find())
        print('region list', region_list[0])
        for skill in developer_skills:
            total_job_count = 0
            technology_data = {
                date: {
                'regions': {},
                'total_job_count': 0
                }
            }
            for region in region_list:
                count = region[date]['technologies'][skill]
                technology_data[date]['regions'][region['region']] = count
                total_job_count += count
            technology_data[date]['total_job_count'] = total_job_count
            technology_collection.find_one_and_update(
                {'technology': skill},
                {'$set': technology_data},
                return_document=ReturnDocument.AFTER
            )
    except Exception as err:
        print(type(err))
        print(err.args)
        print(err)
        raise

# update_technology_data('2023-1-23')

# updating data in mongodb by region
def update_region_data():
    client = MongoClient(MONGO_URI)
    try:
        db = client[DB_NAME]
        region_collection = db['region_data'] 
        scraped_data = scraper()
        date = scraped_data[1]
        for data in scraped_data[0]:
            region_collection.find_one_and_update(
            {'region': data['region']},
            {'$set': {date: data[date]}},
            return_document=ReturnDocument.AFTER)
        update_technology_data(date)
    except Exception as err: 
        print(type(err))
        print(err.args)
        print(err)
        raise
    client.close()

update_region_data()



# update_technology_data('2023-1-23')