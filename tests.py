from sumbert import (summarize, run_test)
#run_test()


text="""
Background CDC is responding to an outbreak of respiratory disease caused by 
a novel ( new ) coronavirus that was first detected in China and which has 
now been detected in more than 100 locations internationally, including 
in the United States. Source and Spread of the Virus Coronaviruses 
are a large family of viruses that are common in people and many 
different species of animals, including camels, cattle, cats, and bats. 
The sequences from U.S. patients are similar to the one that China initially 
posted, suggesting a likely single, recent emergence of this virus from 
an animal reservoir. Some international destinations now have ongoing 
community spread with the virus that causes COVID-19, as do some parts 
of the United States. Community spread means some people have been 
infected and it is not known how or where they became exposed. 
Reported illnesses have ranged from very mild ( including some 
with no reported symptoms ) to severe, including illness 
resulting in death. Older people and people of all ages with severe 
chronic medical conditions -- like heart disease, lung disease 
and diabetes, for example -- seem to be at higher risk of developing 
serious COVID-19 illness. Pandemics happen when a new virus emerges 
to infect people and can spread between people sustainably. Cases 
have been detected in most countries worldwide and community spread 
is being detected in a growing number of countries. In the past century, 
there have been four pandemics caused by the emergence of novel influenza 
viruses. As a result, most research and guidance around pandemics is 
specific to influenza, but the same premises can be applied to the 
current COVID-19 pandemic. Pandemics of respiratory disease follow a 
certain progression outlined in a " Pandemic Intervals Framework. " 
This is a rapidly evolving situation and information will be updated as 
it becomes available. The duration and severity of each phase can vary 
depending on the characteristics of the virus and the public health 
response. CDC and state and local public health laboratories are testing 
for the virus that causes COVID-19. View latest case counts, deaths, 
and a map of states with reported cases. In the absence of vaccine or 
treatment medications, nonpharmaceutical interventions become the 
most important response strategy. Travelers returning from affected 
international locations where community spread is occurring also 
are at elevated risk of exposure, with level of risk dependent on 
where they traveled. People who have serious chronic medical 
conditions like : Heart disease Diabetes Lung disease CDC has developed 
guidance to help in the risk assessment and management of people with 
potential exposures to COVID-19. What May Happen More cases of
 COVID-19 are likely to be identified in the United States in the 
 coming days, including more instances of community spread. 
 Widespread transmission of COVID-19 could translate into large 
 numbers of people needing medical care at the same time. Other 
 critical infrastructure, such as law enforcement, emergency medical 
 services, and sectors of the transportation industry may also be 
 affected. Nonpharmaceutical interventions will be the most important 
 response strategy to try to delay the spread of the virus and reduce 
 the impact of disease. CDC Response Global efforts at this time are 
 focused concurrently on lessening the spread and impact of this virus. 
 The federal government is working closely with state, local, tribal, 
 and territorial partners, as well as public health partners, to respond 
 to this public health threat. CDC is implementing its pandemic 
 preparedness and response plans, working on multiple fronts, 
 including providing specific guidance on measures to prepare 
 communities to respond to local spread of the virus that causes 
 COVID-19. There is an abundance of pandemic guidance developed 
 in anticipation of an influenza pandemic that is being adapted 
 for a potential COVID-19 pandemic. On March 14external icon, a 
 similar policy was issued to include the United Kingdom and the 
 Republic of Ireland. An important part of CDC's role during a 
 public health emergency is to develop a test for the pathogen 
 and equip state and local public health labs with testing capacity. 
 This will allow a greater number of tests to happen close to where 
 potential cases are. CDC Recommends Everyone can do their part to 
 help us respond to this emerging public health threat : Individuals 
 and communities should familiarize themselves with recommendations 
 to protect themselves and their communities from getting and spreading 
 respiratory illnesses like COVID-19. Older people and people with 
 severe chronic conditions should take special precautions because 
 they are at higher risk of developing serious COVID-19 illness. 
 Factors to consider in addition to clinical symptoms may include : 
 Does the patient have recent travel from an affected area ? Has the 
 patient been in close contact with someone with COVID-19 or with 
 patients with pneumonia of unknown cause ? If you are a healthcare 
 provider or a public health responder caring for a COVID-19 patient, 
 please take care of yourself and follow recommended infection 
 control procedures. Your cooperation is integral to the ongoing public 
 health response to try to slow spread of this virus.
"""

print(summarize(text))
