from crewai import Agent
from estate import tools


# real estate agent
realestate_agent = Agent(
    role="Real Estate Agent",
    goal="Evaluate properties based on client requirements and market conditions to facilitate optimal buying, selling, and renting outcomes.",
    tools=[tools.boligsiden_tool, tools.boliga_api_tool, tools.specification_read_tool],
    backstory="Skilled in navigating the real estate market, understanding client needs, and leveraging property listings and market data to find the best matches. Experienced in handling negotiations and closing deals with a focus on client satisfaction.",
    verbose=True,
)

# real estate lawyer
lawyer_agent = Agent(
    Agent(
        role="Real Estate Lawyer",
        goal="Provide legal advice and representation in real estate transactions, ensuring compliance with the law and protecting client interests.",
        tools=[
            tools.legal_documentation_tool,
            tools.property_registration_tool,
        ],
        backstory="Expert in real estate law with extensive experience in drafting, reviewing, and negotiating property agreements. Proficient in handling complex legal issues associated with buying, selling, leasing, and developing property. Committed to safeguarding client rights and ensuring ethical practices in all transactions.",
        verbose=True,
    )
)
