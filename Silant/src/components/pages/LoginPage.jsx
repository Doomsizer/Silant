import React, {useState, useContext, useEffect} from 'react';
import { useNavigate } from 'react-router-dom';
import { AuthContext } from '../AuthContext';
import Header from "../Header";
import Footer from "../Footer";
import "../styles/LoginPage.css"

function LoginPage() {
    const { login } = useContext(AuthContext);
    const [username, setUsername] = useState('');
    const [password, setPassword] = useState('');
    const [error, setError] = useState('');
    const navigate = useNavigate();
    const token = localStorage.getItem('token')
    const isFormValid = username.trim() !== '' && password.trim() !== '';

    useEffect(() => {
        if (token) {
            navigate('/')
        }
    }, [token])

    const handleLogin = async (e) => {
        e.preventDefault();
        const success = await login(username, password);
        if (success) {
            navigate('/');
        } else {
            setError('Неверный логин или пароль');
        }
    };

    return (
        <>
            <Header/>
            <main className="loginMain">
                <h1>Вход</h1>
                <form className="loginForm" onSubmit={handleLogin}>
                    <div>
                        <label>Логин:</label>
                        <input className="loginInput"
                            type="text"
                            value={username}
                            onChange={(e) => setUsername(e.target.value)}
                            placeholder="Введите логин"
                        />
                    </div>
                    <div>
                        <label>Пароль:</label>
                        <input className="loginInput"
                            type="password"
                            value={password}
                            onChange={(e) => setPassword(e.target.value)}
                            placeholder="Введите пароль"
                        />
                    </div>
                    {error && <p style={{ color: 'red' }}>{error}</p>}
                    <button disabled={!isFormValid} className="loginButton" type="submit">Войти</button>
                </form>
            </main>
            <Footer/>
        </>
    );
}

export default LoginPage;