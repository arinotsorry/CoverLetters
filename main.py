"""
Author: Ari Wisenburn
Date: October 18, 2023
"""

import os

intro_paragraph = "Pinpoint specific information that applies to me about the company’s mission, values, description, and about information. Elaborate on how perfect of a fit I am based on my technical skills and character traits. Emphasize skills that overlap between my resume/cover letter and the job description. Do not be obvious about referencing the description directly. Use my existing cover letter as the body of the letter, but add information about how the company’s mission resonates with me before using the template, and add a paragraph at the end about how thankful I am for the opportunity, how great of a fit I would be. Wrap up the cover letter with a professional and optimistic tone. If there is a paragraph of my cover letter irrelevant to the job, briefly summarize it in one or two sentences and try to tie it in to hard skills, technical skills, soft skills, or social skills listed in the job description. Otherwise, for relevant projects and descriptions, tie in as many relevant technical details as possible."
general_cover_letter_body = "In my previous roles, I have consistently demonstrated the ability to balance taking ownership of cross-disciplinary projects from start to finish and facilitating communication between product owners, designers, managers, and other developers. For example, at Wind Talker Innovations, I developed a JavaScript internal testing tool for a mesh network product. This tool enhanced user experience, facilitated data collection at an 85% faster rate, and allowed us to analyze data and make informed data-driven decisions. I also simulated our flagship product using Docker containers and automatically deployed them using Ansible, drastically reducing hardware overhead for onboarding new engineers and scaling testing scenarios. \
  During my internship at Zocdoc, I had the opportunity to lead a React-based user flow redesign, collaborating with cross-functional teams to ensure end-to-end product functionality. I took charge of creating technical documents, integrating new page components, and implementing comprehensive testing procedures. This full-stack experience honed my collaboration skills and made me a more valuable and well-rounded developer. \
  After my last semester, I developed my own website using a tech stack similar to my experience at Zocdoc. This included React, Node.js, Typescript, CSS, and HTML. I created custom components, such as a versatile 'squiggle' component for headers and buttons, and customized existing components from the Chakra UI library. To ensure a smooth user experience, I implemented a CI/CD pipeline using Github Actions to validate my npm build before deploying it to Firebase. This project allowed me to enhance my technical skills and showcase my ability to handle end-to-end development tasks."
specific_cover_letter = """I am writing to express my interest in the Software Engineer position at The Bump, a role that perfectly aligns with my career goals and values. I resonate with The Bump's mission to empower parents and parents-to-be through an inclusive digital platform, and I am eager to contribute my technical expertise to a cause I believe in.
During my internship at Zocdoc, I led a critical initiative to redesign a user flow using a tech stack closely mirroring that of The Bump. This project used React, Node.js, and advanced methodologies. I collaborated closely with designers, product owners, project managers, and fellow developers to translate Figma designs into a fully functional and intuitive user experience. My team used Agile methodologies to estimate and track my progress from project inception to production implementation, ensuring effective collaboration and efficient delivery.
Specifically, my role at Zocdoc showcased my ability to take ownership of a feature from conceptualization to deployment. This experience aligns with the expectations of a Full Stack Software Engineer at The Bump, where I would be collaborating on the development and maintenance of various systems that serve content-oriented web pages and digital tools. My proficiency in React, Next.js, and Node.js positions me to contribute effectively to The Bump's online presence.
To further challenge myself and deepen my understanding of the tech stack and methodologies I learned at Zocdoc, I embarked on a personal project to create my own website from scratch using React. This allowed me to improve my full stack development stills while providing a creative outlet in the UX design. The project demanded an understanding of not only frontend technologies but also seamless integration with backend functionalities.
I admire The Bump's commitment to nurturing a holistic and supportive work environment that prioritizes employee wellbeing and growth. The prospect of contributing my skills to an organization that values collaboration and is dedicated to supporting families during a crucial phase of their lives is exciting. I am confident that my technical skills, adaptability, and dedication to delivering exceptional results make me an ideal fit for this role.
Thank you for considering my application. I am eager to discuss how my experiences and enthusiasm align with The Bump's mission and how I can contribute to your success."""
specific_cover_letter_2 = """I am writing to express my enthusiastic interest in the Full Stack Developer position at Foundry. Foundry Digital’s vision to build the decentralized financial future aligns perfectly with my career goals and my desire to contribute to groundbreaking advancements in the blockchain industry.
In my role as a Full Stack Intern at Zocdoc, I led a critical initiative to redesign a user-facing data capture flow using a tech stack closely resembling that utilized at Foundry, including React and API interfacing. I documented the product structure and how my contribution would fit into the existing architecture, while anticipating pain points and making data-driven decisions on project architecture and metrics collection. Collaborating closely with cross-functional teams, I was able to translate designs into a fully functional and intuitive user experience.
My journey includes significant experience in backend development, especially in Java, JavaScript, Python, and API usage. During my time at WindTalker Innovations, I developed an internal testing tool using JavaScript to sample nodes across a mesh network. As part of this tool’s development, I created new endpoints and edited existing ones for the company’s network API. I collected and processed that data to display intuitive and user-friendly network health assessments accessible to field testers and all levels of leadership. I also used Docker to mock the Ubuntu Linux nodes. After using Ansible to automate and scale this container creation, I increased the company’s network node and testing capacity by two orders of magnitude, while slashing hardware and onboarding costs for other engineers.
I am inspired by the prospect of contributing my skills to an organization that values collaboration, adaptability, and passion in building a better world. I firmly believe that my technical expertise and tenacity to learn combined with my dedication to delivering exceptional results and my alignment with Foundry's values make me a strong fit for this role.
Thank you for considering my application. I am eager to discuss how my experiences and enthusiasm align with Foundry's mission and how I can contribute to your success.
"""
resume = """Contact Information:
- Email: wisenburnari@gmail.com
- Phone: (570) 575-1358
- Website: ariwisenburn.com
- Github: github.com/arinotsorry
- LinkedIn: https://www.linkedin.com/in/ari-wisenburn/


Education:
- Rochester Institute of Technology
- Rochester, NY, 2018-2023
- B.S. Computer Science
- Minor in Electrical Engineering
- Honors program
- Cum laude


Skills:
Backend Skills:
- Java
- Python
- SQL
- C, C++
- REST APIs
- Linux
- Object Oriented Programming (OOP)
- Algorithms
- Data structures
- Web scraping

Frontend Skills:
- React
- Javascript
- Typescript
- HTML/CSS
- GraphQL

Testing Skills:
- CI/CD
- Unit testing/TDD/BDD
- Metrics analytics
- Test Automation using Selenium and Cypress

Other Skills:
- Git and version control systems
- Docker and containerization
- Ansible
- FPGAs
- Verilog/VHDL

Soft Skills:
- Organization
- Creativity
- Prioritization
- Edge-case thinking
- Asking thought provoking and challenging questions
- Critical thinking
- Resourcefulness
- Independence


Work Experience:
Full Stack Intern at Zocdoc - Manhattan, NY 	 		                                                          Jun – Aug 2022
- Managed a React-based user flow redesign from inception to roll-out using Agile methodologies. Authored comprehensive technical documents assessing existing Storybook components and React states. Made strategic recommendations for which features and metrics to implement. Updated components and rewrote Typescript files, leading to a ~77% flow completion rate.
- Implemented TeamCity CI/CD pipeline, which verified extensive unit tests and Cypress UI tests. Established an Optimizely experiment using feature flags and A/B testing to direct and analyze consumer traffic.
- Analyzed page metrics information to visualize website traffic through Datadog metrics dashboards.

Full Stack Co-op Engineering Intern at Wind Talker Innovations - Silver Spring, MD 	 	                                                           Jan – Aug 2021
- Built and maintained the flagship product's production-level internal performance testing tool. Modified Java REST API endpoints in conjunction with JavaScript test script development to collect network performance data asynchronously. Reduced testing time by 85% and extended the tool’s capabilities to become a user-facing feature.
- Automated Docker-Compose image and container creation using Ansible, drastically reducing the hardware costs for onboarding engineers and scaling testing capabilities by two orders of magnitude.

Intern at Black River Systems Company - Utica, NY (Remote) 	 	 	 	                                                       May – Aug 2020
- Programmed a user interface to handle collection, processing, and live heat-map visualization of Radio Frequency data (GPS, Wi-Fi RSSI, and Software Defined Radio signals), which allowed for complete data capture and gave field testers the ability to amend and verify results as they were collected.


Labs & Projects:
Personal Website											   Mar – May 2023
- Constructed an SPA from scratch using React, Typescript, CSS, HTML, and an external UI library.
- Implemented CI/CD pipeline using GitHub Actions to verify build functionality and deploy the Firebase-hosted website.

Wine and Flavor Search Engine									            Jan 2023 – Mar 2023
- Automated Python script with Selenium and BeautifulSoup to automatically scrape multiple wine and flavor webpages for over 10,000 rows of data. Designed a robust MySQL database schema to house wine and flavor information. Developed a Python script to automate data cleansing, table creation, and database population, streamlining the data import process.

Machine Learning Classification Labs								           Aug 2022 – Dec 2022
- Utilize Numpy, Pandas, Scikit-learn, and Tensorflow Python libraries to implement and compare the following classification models: least squares, k-nearest neighbors, random forest, linear squares, support vector machines, linear and Gaussian kernels, multi-layer linear models (with and without rectified linear unit), and multilayer convolutional models.

Personal Safety Android App										                 Feb 2020
- Constructed a personal safety Android application using Android Studio, Kotlin, and Java. Implemented GPS location tracking and SMS features to notify the public safety line if directly prompted or if the failsafe user interaction timer runs out.
- Designated Most Innovative Project at WiC Hacks 2020 for the app's unique features, implementation, and presentation.
"""


def prompt():
    company_name = input("What's the company name?\n")
    position_title = input("What position are you applying for?\n")
    return {"company": company_name, "position": position_title}


info = prompt()
f = open("company.txt", "r")
company_info = f.read()
f.close()

output_prompt = (
    "Generate a page-long cover letter for a "
    + info["position"]
    + " position at "
    + info["company"]
    + ".\n\n"
)
output_prompt += intro_paragraph + "\n\n\n"
output_prompt += (
    "The specific information about the company is:\n" + company_info + "\n\n\n"
)


output_prompt += "My resume is:\n" + resume + "\n\n\n"
output_prompt += (
    "You can sample from this cover letter, but omit information specific to The Bump. The first cover letter sample is:\n"
    + specific_cover_letter
    + "\n\n\n"
    + "You can also incorporate samples from this more technical cover letter, but omit information specific to Foundry. Grab technical descriptions as they are relevant. This cover letter sample is:"
    + specific_cover_letter_2
    + "\n\n\n"
)
output_prompt += (
    "You can also sample from this more general cover letter for technical details:\n"
    + general_cover_letter_body
    + "\n\n\n"
)

prompt_file = open("prompt.txt", "w")
prompt_file.write(output_prompt)
prompt_file.close()
