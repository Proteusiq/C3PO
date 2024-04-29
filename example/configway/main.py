from blogger import BloggerCrew
from utils.events import today


if __name__ == "__main__":
    
    technology = input("Which technology to explore? ")


    inputs = {
        'today': today(),
        'technology': technology,
    }

    crew = BloggerCrew().crew()

    results = crew.kickoff(inputs=inputs)

    print("######################")
    print(results)