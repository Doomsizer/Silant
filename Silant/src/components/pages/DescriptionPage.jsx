import React, { useEffect, useState } from 'react';
import { useParams } from 'react-router-dom';
import axios from 'axios';
import Header from "../Header";
import Footer from "../Footer";

function DescriptionPage() {
    const { type, id } = useParams();
    const [data, setData] = useState(null);
    const [error, setError] = useState('');

    useEffect(() => {
        const fetchDescription = async () => {
            try {
                const token = localStorage.getItem('token');
                const response = await axios.get(`/api/${type}s/${id}/`, {
                    headers: token ? { 'Authorization': `Bearer ${token}` } : {},
                });
                setData(response.data);
            } catch (err) {
                setError('Ошибка загрузки описания');
                console.error(err);
            }
        };
        fetchDescription();
    }, [type, id]);

    if (error) return <p>{error}</p>;
    if (!data) return <p>Загрузка...</p>;

    return (
        <>
            <Header/>
            <main>
                <div>
                    <h1>{data.name}</h1>
                    <p>{data.description}</p>
                </div>
            </main>
            <Footer/>
        </>
    );
}

export default DescriptionPage;