from textwrap import dedent
from crewai import Agent, Task


def search_estate(
    agent: Agent,
    location: str,
    description: str,
) -> Task:
    return Task(
        description=dedent(f"""\
            Analyze the property market in the serene, highly sought-after neighborhood of {location}, based on the property's description: "{description}". Focus on identifying competitive pricing, key selling points like the proximity to top-rated schools, extensive transportation options, and rich cultural surroundings that enhance the property's appeal. Assess the potential demand among families looking for a blend of urban lifestyle and community-oriented living.
            Prepare a detailed market analysis report that highlights how the features of this home align with current market trends and buyer expectations. Include strategies on how to effectively market these features to attract potential buyers."""),
        expected_output=dedent("""\
            A detailed market analysis report that captures the essence of the property's location, its appeal to families, and its competitive positioning in the Copenhagen real estate market. The report should include specific marketing recommendations to target families seeking a high quality of life in an urban setting, emphasizing the home's proximity to education, culture, and transport facilities."""),
        agent=agent,
    )


def evaluate_estate(
    agent: Agent,
    location: str,
    description: str,
) -> Task:
    return Task(
        description=dedent(f"""\
            Review legal documents and regulations related to the property in question at {location}, based on the property's description: "{description}". Focus on ensuring compliance with local zoning laws, property rights, and any special statutes or legal restrictions. Identify potential legal issues and aspects that need addressing before transaction completion.
            Prepare a legal assessment report that summarizes the compliance status, potential risks, and recommended actions to ensure a smooth legal process."""),
        expected_output=dedent("""\
            A comprehensive legal assessment report detailing compliance with local laws, identified legal risks, and suggested measures to mitigate these risks. The report should also outline necessary steps to finalize the property transaction legally and securely."""),
        agent=agent,
    )
