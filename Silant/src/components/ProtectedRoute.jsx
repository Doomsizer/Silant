import React, { useContext } from 'react';
import { Navigate, Outlet } from 'react-router-dom';
import { AuthContext } from './AuthContext';

const ProtectedRoute = ({ requiredRole }) => {
    const { user, loading } = useContext(AuthContext);

    if (loading) return <div>Загрузка...</div>;

    if (!user?.is_authenticated) {
        return <Navigate to="/login" replace />;
    }

    const hasRole = (role) => user.groups?.includes(role);

    if (requiredRole && !hasRole(requiredRole)) {
        return <Navigate to="/unauthorized" replace />;
    }

    return <Outlet />;
};

export default ProtectedRoute;