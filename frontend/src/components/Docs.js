import React from "react";



const Docs = () => {
    return (
        <>
            <div>
                <h1>Project Documentation: Locale API</h1>
                <p>
                    Locale is a developer tool designed to provide 
                    comprehensive geographic information about Nigeria. It offers a range of 
                    functionalities that enable developers to access data on Nigeria's 
                    regions, states, and local government areas (LGAs). This documentation 
                    serves as a guide for understanding and utilizing the 
                    Locale API effectively.
                </p>

                <h3> Table of Contents </h3>
                <ul>
                    <li> <a href="#authentication"> Authentication and Authorization </a> </li>
                    <li> <a href="#search"> Search </a> </li>
                    <li> <a href="#general"> General APIs </a> </li>
                </ul>

                <h3 id="authentication"> Authentication and Authorization </h3>
                <p>
                    Locale API implements authentication and authorization to 
                    ensure secure access to the API endpoints. Developers must 
                    obtain an API key during sign-up, which serves as a 
                    unique identifier for their requests. Including the API key
                    in the request headers is essential for proper 
                    authentication.
                </p>

                <h3 id="search"> Search </h3>
                <p>
                    Locale API offers a powerful search functionality that 
                    allows developers to retrieve information on Nigeria 
                    based on various categories:

                    <ul>
                        <li> Regions:
                            Retrieve information about Nigeria's regions, 
                            including their names, codes, and associated states. 
                        </li>

                        <li> States: Get details about individual states, including 
                            names, codes, and associated local government areas (LGAs). 
                        </li>

                        <li> Local Government Areas (LGAs): Access comprehensive 
                            information about local government areas, such as 
                            names, codes, and related states.
                        </li>
                    </ul>
                </p>

                <h3 id="general"> General APIs </h3>
                <p>
                    Locale API provides general APIs to retrieve comprehensive
                    data sets on Nigeria's regions, states, and LGAs. These APIs 
                    offer an efficient way to access all available information in 
                    a single request. Developers can integrate these APIs into their 
                    applications or services to leverage the complete data set 
                    effectively.
                </p>
            </div>
        </>
    )
}

export default Docs;