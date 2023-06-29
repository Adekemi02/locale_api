#   Locale API
<!-- Back to Top Navigation Anchor -->
<a name="readme-top"></a>

<div align="center">
  <a href="https://github.com/Adekemi02/locale_api">
    
  </a>
</div>

---

<!---Project Logo --->

<div align="center">
  <h1><img src="./images/Locale_screen.PNG" alt="Logo" width="90%" height="40%">
  </h1>
</div>

<div>
  <p align="center">
    <a href="https://github.com/Adekemi02/locale_api/wiki"><strong>Explore the Docs »</strong></a>
    <br />
    <a href="https://github.com/Adekemi02/locale_api/blob/main/images/Local_screen2.png">View Demo</a>
    ·
    <a href="https://github.com/Aadekemi/locale_api/issues">Report Bug</a>
    ·
    <a href="https://github.com/Adekemi02/locale_api/issues">Request Feature</a>
  </p>
</div>

---

<!--- Table of Contents --->

<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-locale-api">About Locale API</a>
      <ul>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li><a href="#lessons-learned">Lessons Learned</a></li>
    <li><a href="#installation">Installation</a></li>
    <li><a href="#usage">Usage</a></li>    
    <li><a href="#sample">Sample</a></li>
    <li><a href="#license">License</a></li>
    <li><a href="#contact">Contact</a></li>
    <li><a href="#acknowledgements">Acknowledgements</a></li>
  </ol>
  <p align="right"><a href="#readme-top">back to top</a></p>
</details>

---

<!-- About the API --->
## About Locale API

Locale is developer tool for anyone who needs to know Nigeria geopraphically. Locale's API shows you all Nigeria's regions, states, and local governement areas (LGAs). Locale is looking to be a handful tool for the thousands of businesses building for Nigeria's 200M+ population size.


This project was built with Python's Flask-RESTX by  by <a href="https://www.github.com/Adekemi02">Barakat Adisa</a> as part of Backend Engineering final Semester Exam and Capstone Project at <a href="https://altschoolafrica.com/schools/engineering">AltSchool Africa</a> 

---

<!-- ### Built With: -->
## Built with

![Flask](https://img.shields.io/badge/flask-%23000.svg?style=for-the-badge&logo=flask&logoColor=white) ![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54) ![MongoDB](https://img.shields.io/badge/-MongoDB-green?logo=mongodb&logoColor=white)

---

<!-- Lessons from the Project -->
## Lessons Learned

Creating this API, I was able to learn and understand the following concepts:
* Caching
* App Deployment with Render
* MongoDB
* Documentation
* Debugging
* Routing
* Database Management
* Rate Limiting
* File Handling
* Redis
* User Authentication
* User Authorization

---

<!-- INSTALLATION -->
## Installation

---

<!-- GETTING STARTED -->
## Usage

To make use of this API, simply follow the following steps:

1. Open the app in your preferred browser by visiting: [https://locale-2o8b.onrender.com](https://locale-2o8b.onrender.com).

2. Create a user account to unlock the full potential of the API.

3. Register as a user by clicking on 'auth' to reveal the dropdown menu for authentication and authorization. You can easily register via the 'api/v1/auth/register' route.

4. Once registered, sign in using the 'api/v1/auth/login' route to generate a JWT token. This token will grant you access to the API. Copy the access token without the quotation marks.

5. Scroll up and click on "Authorize" located at the top right corner. Enter your JWT token in the following format:
   ```
   Bearer thejwtaccesstoken
   ```

6. Click 'Authorize' and then 'Close' to securely authenticate yourself.

7. Now that you are authorized, a world of possibilities awaits! The API provides the following endpoints to cater to your needs:

   - GET /api/v1/states: Retrieve a comprehensive list of all states within Nigeria.
   - GET /api/v1/regions: Discover all geopolitical zones within Nigeria.
   - GET /api/v1/lgas: Access information on all Local Government Areas (LGAs) within each state.
   - GET /api/v1/lgas/{state_id}: Retrieve all local government areas within a specific state.
   - GET /api/v1/regions/{region_id}: Gather in-depth details about an individual region, including its associated states.
   - GET /api/v1/states/{state_id}: Obtain specific information about a single state, along with its metadata.
   - GET /api/v1/search/{query}: Effortlessly search for a region or state by name or ID.

8. When you have completed your API interactions, simply click 'Authorize' once again at the top right corner and proceed to click 'Logout' for a secure and seamless logout experience.

---

<!-- Sample Screenshot -->
## Sample

<div align="center">
  <h1><img src="./images/Locale_screen2.png" alt="Logo">
  </h1>
</div>

---

<div align="center">
  <h1><img src="./images/Locale_screen3.png" alt="Logo">
  </h1>
</div>

---

<!-- License -->
## License

Distributed under the MIT License. See <a href="https://github.com/Adekemi02/locale_api/blob/main/LICENSE">LICENSE</a> for more information.

---

<!-- Contact -->
## Contact

Barakat Adisa - [@adisa_adekhemie](https://twitter.com/adisa_adekhemie) - adisabarakatadekemi@gmail.com

Project Link: [LOCALE API](https://github.com/Adekemi02/locale_api)

---

<!-- Acknowledgements -->
## Acknowledgements

This project was made possible by:

* [AltSchool Africa School of Engineering](https://altschoolafrica.com/schools/engineering)
* [Caleb Emelike's Flask Lessons](https://github.com/CalebEmelike)
* [GitHub Student Pack](https://education.github.com/globalcampus/student)
* [City Population](https://www.citypopulation.de/en/nigeria/admin/)
* [National Bureau of Statistics](https://nigeria.opendataforafrica.org/apps/atlas)
* [Nigeria Data Portal](https://nigeria.opendataforafrica.org/)
* [Wikipedia](https://en.wikipedia.org/wiki/Local_government_areas_of_Nigeria)
