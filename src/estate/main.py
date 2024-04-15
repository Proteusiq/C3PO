from crewai import Crew

from estate.agents import realestate_agent, lawyer_agent
from estate.tasks import search_estate, evaluate_estate


if __name__ == "__main__":
    property_location = input("Where would you like to live?\n> ")
    property_description = input("What is your idea home?\n> ")

    # tasks
    realtor_task = search_estate(
        agent=realestate_agent,
        location=property_location,
        description=property_description,
    )

    lawyer_task = search_estate(
        agent=lawyer_agent,
        location=property_location,
        description=property_description,
    )

    # crew
    crew = Crew(
        agents=[
            realestate_agent,
            # lawyer_agent,
        ],
        tasks=[
            realtor_task,
            # lawyer_task,
        ],
    )

    # launch
    results = crew.kickoff()

    print("Estate Searching Process Completed.")
    print("Selected Estate:")
    print(results)
