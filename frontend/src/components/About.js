import React from 'react';


const About = () => {
    return (
        <>    
            <div className='about-container'>
                <h1>About</h1>
                <p>
                    Locale is a developer tool designed to provide comprehensive 
                    geographic information about Nigeria. Its API enables developers
                    to access data on Nigeria's regions, states, and local 
                    government areas (LGAs). With a population size exceeding 200 
                    million, Locale is a valuable resource for businesses and 
                    developers building applications tailored to Nigeria's diverse 
                    demographics.
                </p>

                <h3>Authentication and Authorization</h3>
                <p>
                    To ensure security, Locale implements authentication and 
                    authorization for API access. Developers must obtain an 
                    API key during sign-up to authenticate their requests. 
                    Each developer is assigned a unique API key, which should 
                    be included in API calls for proper authentication.
                </p>

                <h3>Search</h3>
                <p>
                    Locale offers a search functionality that allows developers
                    to retrieve information on Nigeria based on various 
                    categories, including regions, states, and local government 
                    areas (LGAs). Developers can search for regions along with 
                    their associated states or states along with their 
                    associated LGAs. Locale provides comprehensive metadata 
                    for each region, state, and LGA in the search results.
                </p>

                <h3>General APIs</h3>
                <p>
                    Locale provides APIs for developers to retrieve all regions, 
                    states, and LGAs in Nigeria. These APIs offer a convenient 
                    way to access the complete dataset for integration into 
                    applications and services.
                </p>
            </div>
        </>
    );
};


export default About;