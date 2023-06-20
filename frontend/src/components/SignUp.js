import React, { useState } from "react";
import { Form, Button } from "react-bootstrap";
import "../App.css"
import { Link } from 'react-router-dom';
import { useForm } from "react-hook-form";


const Register = () => {


    const { register, watch, handleSubmit, reset, formState: { errors } } = useForm();

    // const watchName = watch("name", "")
    // console.log(watchName)

    const submitForm = (data) => {
        console.log(data)
        reset()

    }


    return (
        <>
            <div className="container">
                <div className="form">
                    <h1 className="text"> Create Account </h1>

                    <Form>
                        <Form.Group className="mb-3">
                            <Form.Label> Username </Form.Label>
                            <Form.Control 
                                type="text" 
                                placeholder="Enter your username"
                                {...register("username", { required: true, maxLength: 40 })}
                            />
                            {errors.username && <span className="text-danger"> Userame is required </span>}
                            {/* <br /> */}
                            {errors.username?.type === "maxLength" && <span className="text-danger"> Userame cannot exceed 40 characters </span>}
                        </Form.Group>

                        <Form.Group className="mb-3">
                            <Form.Label> Email </Form.Label>
                            <Form.Control 
                                type="email" 
                                placeholder="Enter email address"
                                {...register("email", { 
                                            required: true, 
                                            pattern: /^\S+@\S+$/i,
                                            maxLength: 30
                                        }
                                    )
                                }
                            />
                            {errors.email && <p className="text-danger">
                                <small> Email is required </small> </p>
                            }
                            
                            {errors.email?.type === "pattern" && <p className="text-danger"> 
                                <small> Email is invalid </small> </p>
                            }
                            
                            {errors.email?.type === "maxLength" && <p className="text-danger">
                                <small> Email cannot exceed 30 characters </small>  </p>
                            }
                        </Form.Group>

                        <Form.Group className="mb-3">
                            <Form.Label> Password </Form.Label>
                            <Form.Control 
                                type="password" 
                                placeholder="Enter password"
                                {...register("password", {
                                            required: true,
                                            minLength: 8,
                                        }
                                    )
                                }
                            />
                            {errors.password && <p className="text-danger">
                                <small> Password is required </small> </p>
                            }
                            
                            {errors.password?.type === "minLength" && <p className="text-danger">
                                <small> Password must be at least 8 characters </small>  </p>
                            }
                        </Form.Group>

                        <Form.Group className="mb-3">
                            <Form.Label> Confirm Password </Form.Label>
                            <Form.Control 
                                type="password" 
                                placeholder="Confirm password"
                                {...register("confirmPassword", {
                                            required: true,
                                            minLength: 8,
                                            // validate: (value) => value === "password"
                                        }
                                    )
                                }
                            />
                            {errors.confirmPassword && <p className="text-danger"> 
                                <small> Confirm password is required </small> </p>
                            }
                            
                            {errors.confirmPassword?.type === "minLength" && <p className="text-danger"> 
                                <small> Confirm Password must be at least 8 characters </small> </p>
                            }
                        </Form.Group>
                        
                        <Form.Group className="mb-3">
                            <Button 
                                type="submit" 
                                id="btn-log"
                                className=""
                                onClick={handleSubmit(submitForm)}
                            > 
                                Sign up 
                            </Button>
                        </Form.Group>

                        <Form.Group className="mb-3">
                            <p className="text-muted mt-3 mb-0">
                                Already have an account?{" "}
                                <Link to='/login' className='text btn-lg btn-log'> Login </Link>
                                
                            </p>
                        </Form.Group>
                    </Form>
                </div>
            </div>
        </>
    )
};

export default Register;