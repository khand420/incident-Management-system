// src/components/Register.js
import React, { useState } from 'react';

function Register() {
    const [formData, setFormData] = useState({
        firstName: '',
        lastName: '',
        email: '',
        address: '',
        country: '',
        state: '',
        city: '',
        pincode: '',
        mobileNumber: '',
        fax: '',
        phone: '',
        userType: 'individual',
        password: '',
        confirmPassword: ''
    });

    const [errors, setErrors] = useState({});

    const handleChange = (event) => {
        const { name, value } = event.target;
        setFormData({ ...formData, [name]: value });
    };

    const handleUserTypeChange = (event) => {
        setFormData({ ...formData, userType: event.target.value });
    };

    const validateForm = () => {
        const newErrors = {};
        if (!formData.firstName) newErrors.firstName = "Please enter your first name.";
        if (!formData.lastName) newErrors.lastName = "Please enter your last name.";
        if (!formData.email) newErrors.email = "Please enter a valid email.";
        if (!formData.address) newErrors.address = "Please enter a valid address.";
        if (!formData.country) newErrors.country = "Please select your country.";
        if (!formData.state) newErrors.state = "Please select your state.";
        if (!formData.city) newErrors.city = "Please select your city.";
        if (!formData.pincode) newErrors.pincode = "Please enter a valid pincode.";
        if (!formData.mobileNumber) newErrors.mobileNumber = "Please enter your mobile number.";
        if (!formData.password) newErrors.password = "Password is required.";
        if (formData.password !== formData.confirmPassword) newErrors.confirmPassword = "Confirm password should be the same as password.";
        return newErrors;
    };

    const handleSubmit = (event) => {
        event.preventDefault();
        const validationErrors = validateForm();
        if (Object.keys(validationErrors).length === 0) {
            alert("Form submitted successfully!");
            // Add your form submission logic here
        } else {
            setErrors(validationErrors);
        }
    };

    return (
        <form onSubmit={handleSubmit}>
            <h3>Register</h3>

            <div className="form-group">
                <label></label>
                <div>
                    <label>
                        <input
                            type="radio"
                            value="individual"
                            checked={formData.userType === 'individual'}
                            onChange={handleUserTypeChange}
                        />
                        Individual
                    </label>
                    <label>
                        <input
                            type="radio"
                            value="enterprise"
                            checked={formData.userType === 'enterprise'}
                            onChange={handleUserTypeChange}
                        />
                        Enterprise
                    </label>
                    <label>
                        <input
                            type="radio"
                            value="government"
                            checked={formData.userType === 'government'}
                            onChange={handleUserTypeChange}
                        />
                        Government
                    </label>
                </div>
            </div>

            <input
                type="text"
                name="firstName"
                className="form-control mb-2"
                placeholder="First Name"
                value={formData.firstName}
                onChange={handleChange}
            />
            {errors.firstName && <div className="text-danger">{errors.firstName}</div>}

            <input
                type="text"
                name="lastName"
                className="form-control mb-2"
                placeholder="Last Name"
                value={formData.lastName}
                onChange={handleChange}
            />
            {errors.lastName && <div className="text-danger">{errors.lastName}</div>}

            <input
                type="email"
                name="email"
                className="form-control mb-2"
                placeholder="Email"
                value={formData.email}
                onChange={handleChange}
            />
            {errors.email && <div className="text-danger">{errors.email}</div>}

            <input
                type="text"
                name="address"
                className="form-control mb-2"
                placeholder="Address"
                value={formData.address}
                onChange={handleChange}
            />
            {errors.address && <div className="text-danger">{errors.address}</div>}

            <select
                name="country"
                className="form-control mb-2"
                value={formData.country}
                onChange={handleChange}
            >
                <option value="">Select your country</option>
                <option value="Country1">Country1</option>
                <option value="Country2">Country2</option>
                {/* Add more countries as needed */}
            </select>
            {errors.country && <div className="text-danger">{errors.country}</div>}

            <select
                name="state"
                className="form-control mb-2"
                value={formData.state}
                onChange={handleChange}
            >
                <option value="">Select your state</option>
                <option value="State1">State1</option>
                <option value="State2">State2</option>
                {/* Add more states as needed */}
            </select>
            {errors.state && <div className="text-danger">{errors.state}</div>}

            <select
                name="city"
                className="form-control mb-2"
                value={formData.city}
                onChange={handleChange}
            >
                <option value="">Select your city</option>
                <option value="City1">City1</option>
                <option value="City2">City2</option>
                {/* Add more cities as needed */}
            </select>
            {errors.city && <div className="text-danger">{errors.city}</div>}

            <input
                type="text"
                name="pincode"
                className="form-control mb-2"
                placeholder="Pincode"
                value={formData.pincode}
                onChange={handleChange}
            />
            {errors.pincode && <div className="text-danger">{errors.pincode}</div>}

            <input
                type="text"
                name="mobileNumber"
                className="form-control mb-2"
                placeholder="Mobile Number"
                value={formData.mobileNumber}
                onChange={handleChange}
            />
            {errors.mobileNumber && <div className="text-danger">{errors.mobileNumber}</div>}

            <input
                type="text"
                name="fax"
                className="form-control mb-2"
                placeholder="Fax"
                value={formData.fax}
                onChange={handleChange}
            />

            <input
                type="text"
                name="phone"
                className="form-control mb-2"
                placeholder="Phone"
                value={formData.phone}
                onChange={handleChange}
            />

            <input
                type="password"
                name="password"
                className="form-control mb-2"
                placeholder="Password"
                value={formData.password}
                onChange={handleChange}
            />
            {errors.password && <div className="text-danger">{errors.password}</div>}

            <input
                type="password"
                name="confirmPassword"
                className="form-control mb-2"
                placeholder="Confirm Password"
                value={formData.confirmPassword}
                onChange={handleChange}
            />
            {errors.confirmPassword && <div className="text-danger">{errors.confirmPassword}</div>}

            <button type="submit" className="btn btn-primary">SIGNUP</button>
        </form>
    );
}

export default Register;
