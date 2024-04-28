from datetime import date
from blogger import BloggerCrew


DAY_LOOKUP = {
    '01': 'st',
    '21': 'st',
    '31': 'st',
    '02': 'nd',
    '22': 'nd',
    '03': 'rd',
    '23': 'rd'
}



if __name__ == "__main__":
    
    today = (f"{date.today(): %B %d{DAY_LOOKUP.get('%B', 'th')} %Y}")
    technology = input("Which technology to explore? ")


    inputs = {
        'today': today,
        'technology': technology,
    }

    crew = BloggerCrew().crew()

    results = crew.kickoff(inputs=inputs)

    print("######################")
    print(results)