import logo from "../media/Logotype accent RGB 1.png";
import React, { useContext } from "react";
import "./styles/Header.css";
import { useNavigate, useLocation } from "react-router-dom";
import { AuthContext } from "./AuthContext";

function Header() {
    const navigate = useNavigate();
    const location = useLocation();
    const { user, loading, error } = useContext(AuthContext);
    const { logout } = useContext(AuthContext)

    const toLogin = () => {
        navigate('/login');
    };

    const logOut = () => {
        logout()
    }

    const isLoginPage = location.pathname === '/login';

    return (
        <header>
            <div className="header-top">
                <img className="header-top-logo" src={logo} alt="Логотип компании Силант"/>
                <div className="header-top-info">
                    <span>+7-8352-20-12-09</span>
                    <span>t.me/silant</span>
                </div>
                {user ? (
                    loading ? (
                        <span>Loading</span>
                    ) : error ? (
                        <span className="header-error">{error}</span>
                    ) : (
                        <div className="header-auth">
                            <span className="header-auth-name">{user.username}</span>
                            <button className="header-auth-logout" onClick={logOut}>Выйти</button>
                        </div>
                    )
                ) : (
                    error && !isLoginPage ? (
                        <span className="header-error">Не удалось провести авторизацию, выполните <a href="/login">вход</a> в аккаунт</span>
                    ) : (
                        <button className="header-top-auth" onClick={toLogin}>Войти</button>
                    )
                )}
            </div>
            <div className="header-info">
                <h1>Электронная сервисная книжка "Мой силант"</h1>
            </div>
        </header>
    );
}

export default Header;