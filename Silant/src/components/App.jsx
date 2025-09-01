import React, { Fragment } from 'react';
import { BrowserRouter, Routes, Route } from 'react-router-dom';
import HomePage from './pages/HomePage';
import LoginPage from './pages/LoginPage';
import UnauthorizedPage from './pages/UnauthorizedPage';
import ProtectedRoute from './ProtectedRoute';
import DescriptionPage from './pages/DescriptionPage';
import CarDetailPage from './pages/CarDetailPage';

function App() {
    return (
        <Fragment>
            <BrowserRouter>
                <Routes>
                    <Route path="/login" element={<LoginPage />} />
                    <Route path="/unauthorized" element={<UnauthorizedPage />} />
                    <Route path="/" element={<HomePage />} />
                    <Route path="/description/:type/:id" element={<DescriptionPage />} />
                    <Route path="/car/:id" element={<CarDetailPage />} />
                    <Route element={<ProtectedRoute requiredRole="Manager" />}>
                        <Route path="/admin" element={<div>Админ панель</div>} />
                    </Route>
                </Routes>
            </BrowserRouter>
        </Fragment>
    );
}

export default App;