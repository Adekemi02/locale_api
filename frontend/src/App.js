import React from 'react';
import NavBar from './components/Navbar';
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import './App.css';
import 'bootstrap/dist/css/bootstrap.min.css'
import Home from './components/Home';
import About from './components/About';
import Contact from './components/Contact';
import Docs from './components/Docs';
import Login from './components/Login';
import Logout from './components/Logout';
import Register from './components/SignUp';




const App = () => {

  return (
    <Router>
      <NavBar />

      <Routes>
        <Route path='/' element={<Home />} />

        <Route path='/about' element={<About />} />

        <Route path='/contact' element={<Contact />} />

        <Route path='/docs' element={<Docs />} />

        <Route path='/login' element={<Login />} />

        <Route path='/logout' element={<Logout />} />

        <Route path='/register' element={<Register />} />

      </Routes>

    </Router>
  )
}

export default App;







// useEffect(
  //   () => {
  //     fetch('http://localhost:5000/api/v1/hello')
  //       .then(res => res.json())
  //       .then(data => setMessage(data.message))
  //       .catch(err => console.log(err))
  //   }, []
  // )

  // const [message, setMessage] = useState('')
  // return (
  //   <div className='container'>
  //     <h1> {message} </h1>
  //   </div>
  // )