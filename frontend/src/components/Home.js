import React from 'react';
import { Link } from 'react-router-dom';
import About from './About';
import '../App.css'


const LoggedInLinks = () => {
    return (
        <>
            <div>

            </div>
        </>
    )
}

const Home = () => {
    return (
        <>
            
            <div className='home'>
                <div style={{textAlign: "center"}}>
                    <h1> Welcome to Locale API </h1>
                    <h2> This is a geolocation API for Nigeria </h2>
                </div>
                

                <p className='btn-buttons'>
                    <Link to='/register' className='btn-lg btn-reg'> Get started </Link> 
                    <Link to='/docs' className='btn-lg btn-docs'> Documentation </Link>
                </p>
            </div>

            <div className='home-about' id='about'>
                <About />
            </div>

            
            
        </>
    )
}

export default Home;