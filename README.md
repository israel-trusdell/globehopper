Project
Acme World Travel Inc. has commissioned a project to enable world travelers to research countries of the world prior to embarking on a travel. 
Acme has decided to develop this capability through the presence of a dedicated web site supported by a persistent data store. 
The site will be known as Globe Hopper.

Functional Requirements
    • Ability to search for all countries of the world as a Traveler
    • Ability to search for all countries in a given continent as a Traveler
    • Ability to get details about the capital city of the country  as a Traveler
    • Ability to add/update/delete Country and City information as a Travel Agent  

Non Functional Requirements 
    • 99.99 % availability,  24 * 7

Solution Steps:

Step 1: JIRA - Have all the Functional requirements as JIRA Tickets
    Step 1 (a) : JIRA – Tickets should be traceable to GitHub

Step 2: GitHub  - Create a GlobeHopper repo for the Web App

Step 3: VSCode - Create Project in VSCode and create files as per the design

Step 4: MySQL - Create Database in MySQL
	Step 4(a): Connect to MySQL from application.

Step 5: Python-Flask framework - Code the first API (search for all countries)
	Step 5(a): Postman - Test the API
	Step 5(b): Commit the code into GitHub.
Step 6: Jenkins – Create job to build the project from GitHub and push for code inspection to SonarQube

Step 7: SonarQube – Verify, validate and test the code quality

Step 10: CI/CD – Develop, build and test for code quality for the rest of the API’s (Repeat Steps 5, 6 and 7)

Step 11: TOSCA – Automation of API testing