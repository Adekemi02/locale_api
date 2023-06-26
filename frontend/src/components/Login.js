import React, { useState } from "react";
import { Form, Button } from "react-bootstrap";
import { Link } from 'react-router-dom';
import { useForm } from "react-hook-form";
import {login} from '../auth';
import { useNavigate } from "react-router-dom";
import "../App.css"



const Login = () => {

    const { register, handleSubmit, reset, formState: { errors } } = useForm();

    const navigate = useNavigate();

    const loginUser = (data) => {
        console.log(data)

        const requestOptions = {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify(data)
        }

        fetch('http://localhost:5000/api/v1/auth/login', requestOptions)
            .then(response => response.json())
            .then(data => {
                console.log(data.access_token)
                login(data.access_token)

                navigate('/dashboard')
            })

        reset()
    }

    return (
        <>
            <div className="container">
                <div className="form">
                    <h1 className="text mb-4"> Login </h1>

                    <Form>
                        <Form.Group className="mb-3">
                            <Form.Label> Email </Form.Label>
                            <Form.Control 
                                type="email" 
                                placeholder="Enter email address"
                                {...register("email", { required: true, pattern: /^\S+@\S+$/i})}
                            />
                            {errors.email && <span className="text-danger"> Email is required </span>}
                            {errors.email?.type === "pattern" && <span className="text-danger"> Email is invalid </span>}
                        </Form.Group>

                        <Form.Group className="mb-3">
                            <Form.Label> Password </Form.Label>
                            <Form.Control 
                                type="password" 
                                placeholder="Enter password"
                                {...register("password", {required: true, minLength: 8})}
                            />
                            {errors.password && <span className="text-danger"> Password is required </span>}
                            {errors.password?.type === "minLength" && <span className="text-danger"> 
                                Password must be at least 8 characters </span>}
                        </Form.Group>

                        <Form.Group className="mb-3" controlId="exampleForm.ControlInput1">
                            <Button 
                                type="submit" 
                                id="btn-log"
                                className=""
                                onClick={handleSubmit(loginUser)}
                            > 
                                Login 
                            </Button>
                        </Form.Group>

                        <Form.Group className="mb-3" controlId="exampleForm.ControlInput1">
                            <p className="text-muted mt-3 mb-0">
                                Do not have an account?{" "}
                                <Link to='/register' className='text btn-lg btn-log'> Signup </Link>
                                
                            </p>
                        </Form.Group>

                    </Form>
                </div>
            </div>
        </>
    )
};

export default Login;