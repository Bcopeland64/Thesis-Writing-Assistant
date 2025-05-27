import React from 'react';
import { BrowserRouter, Routes, Route, Navigate } from 'react-router-dom';
import LoginPage from './pages/LoginPage';
import LiteraturePage from './pages/LiteraturePage';
import PrivateRoute from './components/PrivateRoute';
import AuthService from './services/AuthService';
import './App.css'; // Can be removed or modified if default CRA styles are not wanted

const App: React.FC = () => {
    const isLoggedIn = (): boolean => {
        return AuthService.getCurrentUser() !== null;
    };

    return (
        <BrowserRouter>
            <Routes>
                <Route path="/login" element={<LoginPage />} />
                <Route
                    path="/literature"
                    element={
                        <PrivateRoute>
                            <LiteraturePage />
                        </PrivateRoute>
                    }
                />
                <Route
                    path="/"
                    element={
                        isLoggedIn() ? (
                            <Navigate to="/literature" replace />
                        ) : (
                            <Navigate to="/login" replace />
                        )
                    }
                />
            </Routes>
        </BrowserRouter>
    );
};

export default App;
