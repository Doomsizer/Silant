import React, { useState, useEffect } from 'react';
import { useParams } from 'react-router-dom';
import axios from 'axios';
import { Link } from 'react-router-dom';
import Header from "../Header";
import Footer from "../Footer";
import "../styles/HomePage.css";

function CarDetailPage() {
    const { id } = useParams();
    const [carData, setCarData] = useState(null);
    const [maintenances, setMaintenances] = useState([]);
    const [reclaims, setReclaims] = useState([]);
    const [error, setError] = useState('');
    const [loading, setLoading] = useState(true);
    const [activeTab, setActiveTab] = useState('info');

    useEffect(() => {
        const fetchData = async () => {
            setError('');
            setLoading(true);
            try {
                const token = localStorage.getItem('token');
                const carResponse = await axios.get(`/api/cars/${id}/`, {
                    headers: token ? { 'Authorization': `Bearer ${token}` } : {},
                });
                setCarData(carResponse.data);

                const maintenanceResponse = await axios.get('/api/maintenances/', {
                    headers: { 'Authorization': `Bearer ${token}` },
                    params: { car: id },
                });
                setMaintenances(maintenanceResponse.data);

                const reclaimResponse = await axios.get('/api/reclaims/', {
                    headers: { 'Authorization': `Bearer ${token}` },
                    params: { car: id },
                });
                setReclaims(reclaimResponse.data);
            } catch (err) {
                setError('Ошибка загрузки данных');
                console.error(err);
            } finally {
                setLoading(false);
            }
        };
        fetchData();
    }, [id]);

    if (loading) return <p>Загрузка...</p>;
    if (error) return <p>{error}</p>;
    if (!carData) return <p>Машина не найдена</p>;

    const isAuthorizedForFull = carData.contract_number_date || carData.send_date;

    return (
        <>
            <Header/>
            <main>
                <h1>{carData.car_model_name} ({carData.car_number})</h1>
                <div className="button-group">
                    <button className={activeTab === 'info' ? 'active' : ''} onClick={() => setActiveTab('info')}>Инфо</button>
                    <button className={activeTab === 'to' ? 'active' : ''} onClick={() => setActiveTab('to')}>ТО</button>
                    <button className={activeTab === 'reclaims' ? 'active' : ''} onClick={() => setActiveTab('reclaims')}>Рекламации</button>
                </div>
                {activeTab === 'info' && (
                    <div className="car-table-container">
                        <table className="car-table">
                            <thead>
                            <tr>
                                <th>Поле</th>
                                <th>Значение</th>
                            </tr>
                            </thead>
                            <tbody>
                            <tr><td>Заводской номер</td><td>{carData.car_number}</td></tr>
                            <tr><td>Модель машины</td><td>{isAuthorizedForFull ? <Link to={`/description/car-model/${carData.car_model_id}`}>{carData.car_model_name}</Link> : carData.car_model_name}</td></tr>
                            <tr><td>Модель двигателя</td><td>{isAuthorizedForFull ? <Link to={`/description/engine-model/${carData.engine_model_id}`}>{carData.engine_model_name}</Link> : carData.engine_model_name}</td></tr>
                            <tr><td>Номер двигателя</td><td>{carData.engine_number}</td></tr>
                            <tr><td>Модель трансмиссии</td><td>{isAuthorizedForFull ? <Link to={`/description/transmission-model/${carData.trans_model_id}`}>{carData.trans_model_name}</Link> : carData.trans_model_name}</td></tr>
                            <tr><td>Номер трансмиссии</td><td>{carData.trans_number}</td></tr>
                            <tr><td>Модель ведущего моста</td><td>{isAuthorizedForFull ? <Link to={`/description/bridge-model/${carData.main_bridge_model_id}`}>{carData.main_bridge_model_name}</Link> : carData.main_bridge_model_name}</td></tr>
                            <tr><td>Номер ведущего моста</td><td>{carData.main_bridge_number}</td></tr>
                            <tr><td>Модель управляемого моста</td><td>{isAuthorizedForFull ? <Link to={`/description/bridge-model/${carData.sub_bridge_model_id}`}>{carData.sub_bridge_model_name}</Link> : carData.sub_bridge_model_name}</td></tr>
                            <tr><td>Номер управляемого моста</td><td>{carData.sub_bridge_number}</td></tr>
                            {carData.contract_number_date && <tr><td>Номер/дата договора</td><td>{carData.contract_number_date}</td></tr>}
                            {carData.send_date && <tr><td>Дата отгрузки</td><td>{carData.send_date}</td></tr>}
                            {carData.receiver && <tr><td>Получатель</td><td>{carData.receiver}</td></tr>}
                            {carData.address && <tr><td>Адрес</td><td>{carData.address}</td></tr>}
                            {carData.equipment && <tr><td>Комплектация</td><td>{carData.equipment}</td></tr>}
                            {carData.user && <tr><td>Владелец</td><td>{carData.user}</td></tr>}
                            {carData.service_company && <tr><td>Сервисная компания</td><td>{carData.service_company}</td></tr>}
                            </tbody>
                        </table>
                    </div>
                )}
                {activeTab === 'to' && (
                    <div className="car-table-container">
                        <table className="car-table">
                            <thead>
                            <tr>
                                <th>Вид ТО</th>
                                <th>Дата ТО</th>
                                <th>Наработка, м/час</th>
                                <th>Номер заказа-наряда</th>
                                <th>Дата заказа-наряда</th>
                                <th>Сервисная компания</th>
                            </tr>
                            </thead>
                            <tbody>
                            {maintenances.map(maintenance => (
                                <tr key={maintenance.id}>
                                    <td>{maintenance.type.name}</td>
                                    <td>{maintenance.maintenance_date}</td>
                                    <td>{maintenance.worked_for}</td>
                                    <td>{maintenance.order_number}</td>
                                    <td>{maintenance.order_date}</td>
                                    <td>{maintenance.service_company.username}</td>
                                </tr>
                            ))}
                            </tbody>
                        </table>
                    </div>
                )}
                {activeTab === 'reclaims' && (
                    <div className="car-table-container">
                        <table className="car-table">
                            <thead>
                            <tr>
                                <th>Дата отказа</th>
                                <th>Наработка, м/час</th>
                                <th>Узел отказа</th>
                                <th>Описание отказа</th>
                                <th>Способ восстановления</th>
                                <th>Используемые запасные части</th>
                                <th>Дата восстановления</th>
                                <th>Время простоя техники</th>
                                <th>Сервисная компания</th>
                            </tr>
                            </thead>
                            <tbody>
                            {reclaims.map(reclaim => (
                                <tr key={reclaim.id}>
                                    <td>{reclaim.broke_date}</td>
                                    <td>{reclaim.worked_for}</td>
                                    <td>{reclaim.broke_place.name}</td>
                                    <td>{reclaim.broke_description}</td>
                                    <td>{reclaim.restore_method.name}</td>
                                    <td>{reclaim.used_spare_parts}</td>
                                    <td>{reclaim.restore_date}</td>
                                    <td>{reclaim.downtime}</td>
                                    <td>{reclaim.service_company.username}</td>
                                </tr>
                            ))}
                            </tbody>
                        </table>
                    </div>
                )}
            </main>
            <Footer/>
        </>
    );
}

export default CarDetailPage;