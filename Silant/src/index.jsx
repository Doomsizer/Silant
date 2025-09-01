import React from "react";
import { createRoot } from 'react-dom/client';
import App from "./components/App";
import { AuthProvider } from './components/AuthContext';

const container = document.getElementById("root");
if (container) {
    const root = createRoot(container);
    root.render(
        <AuthProvider>
            <App />
        </AuthProvider>
    );
}