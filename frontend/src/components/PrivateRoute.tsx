import React from 'react';
import { Navigate, Outlet } from 'react-router-dom';
import AuthService from '../services/AuthService';

const PrivateRoute: React.FC = () => {
    const currentUser = AuthService.getCurrentUser(); // Checks for token in localStorage

    return currentUser ? <Outlet /> : <Navigate to="/login" replace />;
};

export default PrivateRoute;
