import React, { createContext, useState, useEffect } from 'react';
import axios from 'axios';

const AuthContext = createContext();

function AuthProvider({ children }) {
    const [user, setUser] = useState(null);
    const [loading, setLoading] = useState(false);
    const [error, setError] = useState(null);

    const login = async (username, password) => {
        setLoading(true);
        setError(null);
        try {
            const response = await axios.post('/api/token/', { username, password });
            const token = response.data.access;
            localStorage.setItem('token', token);
            await fetchUserInfo(token);
        } catch (err) {
            setError('Ошибка логина');
            console.error(err);
        } finally {
            setLoading(false);
        }
    };

    const logout = () => {
        localStorage.removeItem('token');
        setUser(null);
        setError(null);
    };

    const fetchUserInfo = async (token) => {
        setLoading(true);
        setError(null);
        try {
            const response = await axios.post('/api/user-info/', { token }, {
                headers: { 'Content-Type': 'application/json' }
            });
            setUser({ ...response.data, is_authenticated: true });
        } catch (err) {
            setError('Ошибка получения данных пользователя');
            console.error(err);
            localStorage.removeItem('token');
            setUser(null);
        } finally {
            setLoading(false);
        }
    };

    useEffect(() => {
        const token = localStorage.getItem('token');
        if (token && !user) {
            fetchUserInfo(token);
        }
    }, [user]);

    return (
        <AuthContext.Provider value={{ user, login, logout, loading, error }}>
            {children}
        </AuthContext.Provider>
    );
}

export { AuthContext, AuthProvider };