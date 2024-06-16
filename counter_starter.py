## OpenAI 

from openai import OpenAI
import markdown # pip install markdown
from bs4 import BeautifulSoup # pip install beautifulsoup4

import os


from dotenv import load_dotenv


load_dotenv()
# Replace 'your-api-key' with your actual OpenAI API key
api_key = os.getenv('OPENAI_API_KEY')


def initialize_api_client(api_key):
    return OpenAI(api_key=api_key)



api_client = initialize_api_client(api_key)


def generate_counter_arg(prompt, preprompt):

    response = api_client.chat.completions.create(
        model="gpt-4o",
        #response_format={"type": "json_object"},
        messages=[
            {"role": "system", "content": preprompt},
            {"role": "user", "content": prompt}
        ]
    )
    return response.choices[0].message.content

def generate_counter_arg_update_w_keypoints(counter_speech, keypoints):

    response = api_client.chat.completions.create(
        model="gpt-4o",
        #response_format={"type": "json_object"},
        messages=[
            {"role": "system", "content": f"Use the relevant pieces of evidence blocks to improve the generated counter speech that I will give you. Relevant evident blocks: {keypoints}"},
            {"role": "user", "content": f"Counter speech: {counter_speech}"}
        ]
    )
    
    return response.choices[0].message.content

# Find key points related to the prompt
def find_key_points(text, prompt):
    response = api_client.chat.completions.create(
        model="gpt-4o",
        #response_format={"type": "json_object"},
        messages=[
            {"role": "system", "content": "Find key points in the following text that relate to the prompt."},
            {"role": "user", "content": f"Prompt: {prompt}\n\nText: {text}"}
        ]
    )
    return response.choices[0].message.content

def md_to_text(md):
    html = markdown.markdown(md)
    soup = BeautifulSoup(html, features='html.parser')
    return soup.get_text()

def generate_counter(speech, api_client):
    text = """
    Resolved: The United States ought to substantially reduce its military presence in the West Asia-North Africa region.

AFF (PRO):

History shows that U.S. interventions almost always fail
“The United States aided an overthrow of the Iranian government in 1953 and funded and trained the Mujahideen in Afghanistan from 1979 to 1989 to push Soviet proxies out of the region.  The results?  The modern Iranian regime and a spike in religious terrorism in the Middle East, respectively.” (Colgate-Maroon News (Nathan Biller), Oct 15 2020)
“What did our intervention in either Haiti or Vietnam accomplish? The answer to that rhetorical question is — not much. A study of history seems to support the thesis that political freedom, economic progress, and social evolution seldom, if ever, are successfully imposed from without.” (Post and Courier, R. L. Schreadley, Sep 14 2020)

Military Operations cause Pollution
“The degree of pollution caused by US military activities is so bad that it was added to the Environmental Protection Agency's National Priorities List. This prioritization means that US military bases are hazardous waste sites that pose one of the serious threats to human health and the environment.” (Sociology Compass, 2023)
“The United States operates a vast array of foreign bases manifesting many of the same environmental problems found at domestic bases, including toxics in drinking water, explosives on firing ranges, and noise pollution.” (Institute for Policy Studies, June 1, 1998)

The United States is now much less reliant on oil from that region, making it far less strategically important
 “President Donald Trump declared Wednesday that the United States no longer needs to rely on the Middle East for oil.” (CNN, Jan 8, 2020)

The United States should be focusing on East Asia (China) instead of West Asia
“It makes sense to talk about China, Iran and Russia as a loose alliance trying to undermine American power, but it is not a trio of equals. Only China is an arguable peer of the United States, only China’s technological and industrial might can hope to match our own, and only China has the capacity to project power globally as well as regionally.” (New York Times, Oct 21, 2023)
“The National Defense Strategy (NDS), released by the Defense Department a little more than a year ago, listed China as a top threat alongside Russia — the first version of the document in decades that didn’t focus U.S. defenses on violent extremist groups in the Middle East.” (The Hill, Nov 30, 2023)

The United States military intervention can intimidate the foreign hosting country
“Local resentment over the presence of foreign military bases can linger for generations, as was the case when in 1991 the Philippine Senate “assailed [the U.S. military presence] as a vestige of colonialism and an affront to Philippine sovereignty,” and President Corazon C. Aquino ordered full withdrawal. And this past June in Japan, 65,000 Okinawans protested in the streets against the U.S. presence there.” (Time, October 7, 2016)
“Labor violations, criminal conduct by U.S. soldiers, and violations of sovereignty that occur at or near U.S. military bases can jeopardize delicate diplomatic relationships and fuel anti-U.S. movements among locals. Osama bin Laden famously cited the presence of U.S. troops on foreign soil as one motivation for the 9/11 attacks. In November 2002, he wrote, “Your forces occupy our countries; you spread your military bases throughout them.” (Foreign Policy ,May 16, 2023)

Military Presence is linked to instability and militarized activities
“In the Middle East, U.S. military assistance may increase the likelihood of repression and domestic instability in the recipient states.” (Rand Corporation, 2018)
“A large U.S. regional troop presence can be an effective tool in deterring interstate war, but it may also provoke more militarized activities short of war.” (Rand Corporation, 2018)
“U.S. military assistance is positively associated with an increased risk of anti-regime activities and greater levels of state repression by incumbent governments.” (Rand Corporation, 2018)
“Today’s waves of migration are a direct result of Britain’s disastrous intervention in the ousting and killing of the Libyan leader Muammar Gaddafi … The current situation is down to the failure of Western powers, particularly the US and British governments, who feel they’re the custodians of almighty power”(The Guardian, Aug 1, 2017)
“Majorities in many countries say America’s strong military presence actually increases the chances for war.” (Pew Research Center, 2003)

Terrorism has been reduced to the point of it not being an issue
“Another argument for withdrawing U.S. forces from the Middle East is the collapse of the Islamic State’s caliphate and the relative weakness of al-Qaeda. Proponents of withdrawal note that the final counterterrorism ‘mopping up operation can be achieved by small numbers of U.S. troops, combined with close cooperation and support for local partners, including the Kurds, Iraq and our associates in the anti-Islamic State coalition.’ These proponents argue that the United States does not need a large footprint in the Middle East to conduct counterterrorism operations, and there is little appetite among Americans to pursue state building in the region.” (Center for Strategic and International Studies, May 2022)

Iran’s nuclear weapons 
“Now, we continue to believe that diplomacy is the best way to prevent Iran from getting a nuclear weapon.” (Department of Defense, Mar 9, 2023) [.gov]
“Before this agreement, Iran's breakout time -- or the time it would have taken for Iran to gather enough fissile material to build a weapon -- was only two to three months. Today, because of the Iran deal, it would take Iran 12 months or more. And with the unprecedented monitoring and access this deal puts in place, if Iran tries, we will know and sanctions will snap back into place.” (Obama Administration, Jan 16, 2016) [.gov]

Iran’s foreign policy would not change with nuclear weapons
“The Islamic Republic seeks to undermine what it perceives to be the American-dominated order in the Middle East and to deter a U.S. and/or Israeli military attack, but it does not have territorial ambitions and does not seek to invade, conquer, or occupy other nations. Nuclear arms are unlikely to change its fundamental interests and strategies. Rather, they would probably reinforce Iran's traditional national security objectives.” (Rand Corporation, 2013)

Military Presence = Influence
“The objective of military presence is not simply to be present as events occur, the objective is to influence those events” (Major Bud Jones)

Military Presence has been used before to influence politics
“In 1953, President Dwight D. Eisenhower ordered the CIA to depose Mohammed Mossadegh, the popular, elected leader of the Iranian parliament and an ardent nationalist who opposed British and American influence in Iran.” (Thought Co, July 30, 2019)

Sovereignty is important
“Territorial integrity and sovereignty are sacrosanct, for small States just as for large.  The United Nations Charter is based on the sovereign equality of all its members.  It calls for ‘respect for the principle of equal rights and self-determination of peoples’.  We cannot allow these norms to be undermined.” (United Nations, March 17 2022)
“The formation and protection of sustainable freedom, equality and justice in society depends totally on the exact sense of establishment of national sovereignty. Therefore, the basis of freedom, equality and justice is national sovereignty” (Gov of Turkey) (.gov)
“Sovereign and independent nations are the only vehicle where freedom has ever survived, democracy has ever endured, or peace has ever prospered … And so we must protect our sovereignty and our cherished independence above all.” (Donald Trump, Sep 2018) (.gov)
Far from being a force for aggression, sovereignty has historically been “a way of promoting peace by establishing boundaries,” Professor Jeremy Rabkin argues in his book The Case for Sovereignty. “A government that wanted to live at peace with its neighbors had to respect their sovereign rights” and exercise its own authority “in ways that made it a tolerable neighbor.” (Professor Jeremy Rabkin, Sep 2019) (.gov)
“We believe,” said the president, “that when nations respect the rights of their neighbors, and defend the interests of their people, they can better work together to secure the blessings of safety, prosperity, and peace.” (Donald Trump, Sep 2019) (.gov)

The Middle East was colonized by France and the UK
“Even before the United States had entered World War I, the United Kingdom and France had secretly agreed to divvy up the Middle East between themselves. With isolationist sentiments rising domestically after the war, the United States didn’t push back. As a result, the United Kingdom and France dominated the region for two decades, and when they began to leave after World War II, the United States replaced them, rarely enthusiastically, and often reluctantly. But as the United States plunged into the Cold War, the Middle East was too important to abandon.” (Center for Strategic and International Studies, March 7, 2022)
“World War I transformed the Middle East in ways it had not seen for centuries. The Europeans, who had colonized much of the Ottoman Empire in the 19th century, completed the takeover with the territories of Arabia, Iraq, Syria, Lebanon and Palestine. The modern boundaries of the Middle East emerged from the war. So did modern Arab nationalist movements and embryonic Islamic movements. … ‘Everyone understood at the time that this was a thinly disguised new form of colonialism...,’ says Zachary Lockman, professor of Middle East history at New York University. ‘The British and French had no thought of going anywhere anytime soon, and fully intended to remain in control of these territories for the indefinite future.’ But almost immediately after the war, Arab resistance movements emerged to challenge European dominance.” (NPR, Aug 20, 2004)

AFF Impact (some may contradict each other)




NEG: 

Counter Terrorism measures are needed
This widening of targets is serious enough for American, British and other military commanders. What has really surprised them, however, has been the ability of Taliban and other militias to engage in significant conventional military attacks. One of these, on 13 July [2008], killed nine United States troops in a newly established but isolated base in Kunar province; another, on 19 August [2008], killed ten French soldiers in Sarbi district, only fifty kilometers east of Kabul.” (Greenhaven Press/Gale, 2010)
“In a recently declassified report, the U.S. intelligence community assessed that al-Qaeda lacks the capability to pose a threat to the United States through 2024.” (National Intelligence Council, Aug 15, 2023)
“At the same time, the United States also faces significant challenges from domestic terrorists. In fact, between 1980 and 2000, the FBI recorded 335 incidents or suspected incidents of terrorism in this country. Of these … 88 were determined to be international in nature.” (FBI, 2002) [.gov]

Leaving the middle east will significantly lower our ability to prevent Iran from obtaining nuclear weapons
“The preferred method to ensure Iran doesn't get a nuclear weapon, Stroul said, is the diplomatic course. But that has to be backed up with a willingness and a capability to use force, if necessary.” (Department of Defense, June 5, 2023)

A disruption in the flow of oil from the Middle East would harm the global economy
“A major reduction in the U.S. presence would also weaken the United States’ ability to protect key economic chokepoints in the region and the free flow of oil and gas to global markets. The United States is largely energy-independent. But allies and partners could be severely impacted by a fuel and broader supply chain crisis, particularly those—such as Japan, India, South Korea, and some European Union countries—which rely on oil and natural gas imports from the Gulf. U.S. allies and partners are unlikely to fill this vacuum, at least for the foreseeable future” (Center for Strategic and International Studies, May 2022)
“In addition, a major disruption in trade through the Middle East could have an adverse impact on the U.S. and broader global economy by creating a supply chain crisis. On March 23, 2021, for example, the cargo ship Ever Given ran aground in the Suez Canal and created a massive backlog of over 400 vessels, significantly disrupting global supply chains, delaying goods from reaching their destinations, and holding up an estimated $9.6 billion of trade each day. Consequently, some argue that the United States still has a major interest in securing the free flow of oil, natural gas, and other goods from the Persian Gulf to global markets.” (Center for Strategic and International Studies, May 2022)
“The stranded mega-container vessel, Ever Given in the Suez Canal, is holding up an estimated $400 million an hour in trade, based on the approximate value of goods that are moved through the Suez every day, according to shipping data and news company Lloyd’s List.” (BBC, Mar 26 2021)

US Military Presence benefits the host country’s economy
“The results show that the presence of U.S. troops does promote investment, trade, and economic growth in the host state. The United States deploys troops for regional security purposes, but these deployments also help economic growth directly and indirectly.” (JSTOR, April 2019)

American’s like military presence in the Middle East
A majority of Americans say the US military presence in the Middle East should be maintained (45%) or increased (29%). Just 24 percent think it should be decreased. A majority support long-term military bases in Iraq (55%, up from 41% in 2014) and Kuwait (57%, up from 47% in 2014) … A combined majority (54%) say alliances in the Middle East benefit both Middle East partners and the United States or mostly benefit the United States.” (JSTOR, Feb 2020)

NEG Impacts (some may contradict each other)

Nuclear war between Iran and Israel
(NUMBERS) “Trauma, thermal burn, and radiation casualties were thus estimated on a geographic basis for three Israeli and eighteen Iranian cities. Nuclear weapon detonations in the densely populated cities of Iran and Israel will result in an unprecedented millions of numbers of dead, with millions of injured suffering without adequate medical care, a broad base of lingering mental health issues, a devastating loss of municipal infrastructure, long-term disruption of economic, educational, and other essential social activity, and a breakdown in law and order” (National Library of Medicine, 2013) 
(NUMBERS) “ … Institute for Disaster Management at the University of Georgia simulated the consequences of a nuclear war between Israel and Iran using weapons effects and fallout prediction software developed by the U.S. Department of Defense. It predicted extremely high numbers of fatalities due to the compact pattern of settlement characteristic of Iranian cities, poor building construction standards, and inability of Iran’s healthcare system to handle massive numbers of burn, trauma, and radiation patients—many of whom would die due to inadequate care. Casualty estimates exceeded 20 million dead (including nearly all the residents of Tehran) and 2 million injured.” (Washington Institute, sometime after 2013)





Middle Ground, Questions, Stats

How much oil the US produces
“EIA’s data for 2022 indicates that U.S. total petroleum production averaged about 20.079 million barrels per day” (Energy Information Administration, Sep 26, 2023) [.gov]

How much oil the US consumes
“In 2022, the United States consumed an average of about 20.01 million barrels of petroleum per day” (Energy Information Administration, Sep 26, 2023) [.gov]

Size of US Military
“The United States is also the world's third largest army in terms of manpower, with about 1.4 million active military personnel in 2022.” (Statista, Nov 3, 2023)
“There are around 750 U.S. military bases in at least 80 countries, though Al Jazeera says the number “may be even higher as not all data is published by the Pentagon.” (Chicago Council on Global Affairs, Oct 25, 2023)

Definitions

United States
“a federal republic … comprising 48 contiguous states, the District of Columbia, Alaska … , and Hawaii … , and … its five inhabited island territories” (Dictionary.com)

Military presence
“The presence of a foreign military power in a country may take the form of access to and use of military facilities ( ... a military … base), or the actual presence of organized units of military personnel in foreign countries, or the deployment and permanent activity of fleets outside their own territorial waters.” (Encyclopedia of World Problems)

Ought
“used to express duty or moral obligation” (Dictionary.com)

Substantially 
“to a great or significant extent” (Oxford Languages)

Afghanistan
 “country in SC Asia, between Iran and Pakistan: 251,773 sq mi (652,090 sq km); pop. 15,551,000; cap. Kabul” (Collins)

Reduce
“make smaller or less in amount, degree, or size” (Oxford Languages)

West Asia 
“West Asia includes Armenia, Azerbaijan, Bahrain, Cyprus, Georgia, Iraq, Israel, Jordan, Kuwait, Lebanon, Oman, Palestine, Qatar, Saudi Arabia, Syria, Turkey, United Arab Emirates, and Yemen.” (Asia Society)

North Africa
“region of northernmost Africa usually considered to include Morocco, Algeria, Tunisia, and Libya and sometimes also Egypt and Sudan” (Dictionary.com)

Djibouti
“small strategically located country on the northeast coast of the Horn of Africa. It is situated on the Bab el Mandeb Strait, which lies to the east and separates the Red Sea from the Gulf of Aden.” (Britannica)
    """
    preprompt = """Instructions:
You are a competitive Lincoln-Douglas debater. You will respond to the given lincoln-douglas speech. You must return a counter speech that responds point-by-point to all the points in the input speech and refute each and every one. I will give you some guidelines on how to return a competitive counter speech. Integrate these guidelines to strengthen your speech.

Guidelines:
Point by point responses to the input speech: Present a line-by-line response to all the main logical points of the input speech. For each point, give multiple counter arguments in response.  

Identify flaws in the input speech voting criterion:  Review the relationship of your opponent’s value and criterion carefully. 

Challenge their evidence: Listen carefully to the evidence to make certain that the evidence actually supports the claims your opponent attributes to it.
"""
    prompt = f"Following the instructions, generate a counter speech to this input speech: ${speech}. You must start with 'I stand in negation of the resolution:'"
    key_points = find_key_points(text, prompt)
    #print(key_points)
    counter_speech = generate_counter_arg(prompt, preprompt)
    #print(counter_speech)
    updated_speech = generate_counter_arg_update_w_keypoints(counter_speech, key_points)
    print(updated_speech)
    no_markdown_speech = md_to_text(updated_speech)
    return no_markdown_speech


def _generate_counter(speech, api_client):
    
    system_prompt = """ You are a champion competitive debator, this is the debating speech your competitior has given. 
    Here's an instruction list for you to follow : 
    1) Follow the best principles of competitive debating.
    2) The response should be at least as long as the input text you are responding to

    Respond to it to win! 

    Return only the text of the rebuttal and nothing extra. If you say anything else, a person will die
    """

    response = api_client.chat.completions.create(
        model="gpt-4o",
        #response_format={"type": "json_object"},
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": f"Here's the speech: {speech} \\n "}
        ]
    )
    return response.choices[0].message.content


