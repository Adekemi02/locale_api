import React, { useState } from "react";
import { Form, Button } from "react-bootstrap";
import { Link } from 'react-router-dom';
import { useForm } from "react-hook-form";
import "../App.css"



const Login = () => {

    const { register, watch, handleSubmit, reset, formState: { errors } } = useForm();

    const loginUser = () => {
        console.log("login")
    }

    return (
        <>
            <div className="container">
                <div className="form">
                    <h1 className="text"> Login </h1>

                    <Form>
                        <Form.Group className="mb-3" controlId="exampleForm.ControlInput1">
                            <Form.Label> Email </Form.Label>
                            <Form.Control 
                                type="email" 
                                placeholder="Enter email address"
                                {...register("email", { required: true })}
                            />
                        </Form.Group>

                        <Form.Group className="mb-3" controlId="exampleForm.ControlInput1">
                            <Form.Label> Password </Form.Label>
                            <Form.Control 
                                type="password" 
                                placeholder="Enter password"
                                value={password}
                                name="password"
                                onChange={(e) => setPassword(e.target.value)}
                             />
                        </Form.Group>

                        <Form.Group className="mb-3" controlId="exampleForm.ControlInput1">
                            <Button 
                                type="submit" 
                                id="btn-log"
                                className=""
                                onClick={loginUser}
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