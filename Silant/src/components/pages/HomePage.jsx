import React, { useContext, useState, useEffect } from 'react';
import { AuthContext } from '../AuthContext';
import "../styles/HomePage.css";
import Header from "../Header";
import Footer from "../Footer";
import axios from 'axios';
import { Link } from 'react-router-dom';

function HomePage() {
    const { user } = useContext(AuthContext);
    const [searchNumber, setSearchNumber] = useState('');
    const [cars, setCars] = useState([]);
    const [maintenances, setMaintenances] = useState([]);
    const [reclaims, setReclaims] = useState([]);
    const [carData, setCarData] = useState(null);
    const [error, setError] = useState('');
    const [loading, setLoading] = useState(true);
    const [activeTab, setActiveTab] = useState('info');

    const [carFilters, setCarFilters] = useState({
        car_model_name: '',
        engine_model_name: '',
        trans_model_name: '',
        sub_bridge_model_name: '',
        main_bridge_model_name: ''
    });

    const [maintenanceFilters, setMaintenanceFilters] = useState({
        type: '',
        car_number: '',
        service_company: ''
    });

    const [reclaimFilters, setReclaimFilters] = useState({
        broke_place: '',
        restore_method: '',
        service_company: ''
    });

    useEffect(() => {
        if (user && !user.groups.includes('Manager')) {
            fetchBoundedData();
        } else {
            setLoading(false);
        }
    }, [user]);

    const fetchBoundedData = async () => {
        setError('');
        setLoading(true);
        try {
            const token = localStorage.getItem('token');
            if (!token) {
                setError('Необходимо авторизоваться');
                setLoading(false);
                return;
            }
            const carsResponse = await axios.get('/api/cars/', {
                headers: { 'Authorization': `Bearer ${token}` },
            });
            const sortedCars = carsResponse.data.sort((a, b) => new Date(b.send_date) - new Date(a.send_date));
            setCars(sortedCars);

            const maintenancesResponse = await axios.get('/api/maintenances/', {
                headers: { 'Authorization': `Bearer ${token}` },
            });
            const sortedMaintenances = maintenancesResponse.data.sort((a, b) => new Date(b.maintenance_date) - new Date(a.maintenance_date));
            setMaintenances(sortedMaintenances);

            const reclaimsResponse = await axios.get('/api/reclaims/', {
                headers: { 'Authorization': `Bearer ${token}` },
            });
            const sortedReclaims = reclaimsResponse.data.sort((a, b) => new Date(b.broke_date) - new Date(a.broke_date));
            setReclaims(sortedReclaims);
        } catch (err) {
            setError('Ошибка загрузки данных');
            console.error(err);
        } finally {
            setLoading(false);
        }
    };

    const handleSearch = async () => {
        setError('');
        setCarData(null);
        try {
            const token = localStorage.getItem('token');
            const response = await axios.get(`/api/cars/?car_number=${searchNumber}`, {
                headers: token ? { 'Authorization': `Bearer ${token}` } : {},
            });
            if (response.data.length > 0) {
                setCarData(response.data[0]);
            } else {
                setError('Машина не найдена');
            }
        } catch (err) {
            setError('Ошибка поиска');
            console.error(err);
        }
    };

    const handleCarFilterChange = (e) => {
        const { name, value } = e.target;
        setCarFilters({ ...carFilters, [name]: value });
    };

    const handleMaintenanceFilterChange = (e) => {
        const { name, value } = e.target;
        setMaintenanceFilters({ ...maintenanceFilters, [name]: value });
    };

    const handleReclaimFilterChange = (e) => {
        const { name, value } = e.target;
        setReclaimFilters({ ...reclaimFilters, [name]: value });
    };

    const filteredCars = cars.filter(car =>
        car.car_model_name.toLowerCase().includes(carFilters.car_model_name.toLowerCase()) &&
        car.engine_model_name.toLowerCase().includes(carFilters.engine_model_name.toLowerCase()) &&
        car.trans_model_name.toLowerCase().includes(carFilters.trans_model_name.toLowerCase()) &&
        car.sub_bridge_model_name.toLowerCase().includes(carFilters.sub_bridge_model_name.toLowerCase()) &&
        car.main_bridge_model_name.toLowerCase().includes(carFilters.main_bridge_model_name.toLowerCase())
    );

    const filteredMaintenances = maintenances.filter(maintenance =>
        maintenance.type.name.toLowerCase().includes(maintenanceFilters.type.toLowerCase()) &&
        maintenance.car.car_number.toLowerCase().includes(maintenanceFilters.car_number.toLowerCase()) &&
        maintenance.service_company.username.toLowerCase().includes(maintenanceFilters.service_company.toLowerCase())
    );

    const filteredReclaims = reclaims.filter(reclaim =>
        reclaim.broke_place.name.toLowerCase().includes(reclaimFilters.broke_place.toLowerCase()) &&
        reclaim.restore_method.name.toLowerCase().includes(reclaimFilters.restore_method.toLowerCase()) &&
        reclaim.service_company.username.toLowerCase().includes(reclaimFilters.service_company.toLowerCase())
    );

    const isAuthorizedForFull = carData && (carData.contract_number_date || carData.send_date);

    if (loading) return <p>Загрузка...</p>;

    return (
        <>
            <Header/>
            <main>
                <p className="main-info">Проверьте комплектацию и технические характеристики техники Силант</p>
                {user && !user.groups.includes('Manager') ? (
                    <>
                        <div className="button-group">
                            <button className={activeTab === 'info' ? 'active' : ''} onClick={() => setActiveTab('info')}>Инфо</button>
                            <button className={activeTab === 'to' ? 'active' : ''} onClick={() => setActiveTab('to')}>ТО</button>
                            <button className={activeTab === 'reclaims' ? 'active' : ''} onClick={() => setActiveTab('reclaims')}>Рекламации</button>
                        </div>
                        {error && <span className="error">{error}</span>}
                        {activeTab === 'info' && (
                            <>
                                <div className="filters">
                                    <input type="text" name="car_model_name" placeholder="Модель техники" value={carFilters.car_model_name} onChange={handleCarFilterChange} />
                                    <input type="text" name="engine_model_name" placeholder="Модель двигателя" value={carFilters.engine_model_name} onChange={handleCarFilterChange} />
                                    <input type="text" name="trans_model_name" placeholder="Модель трансмиссии" value={carFilters.trans_model_name} onChange={handleCarFilterChange} />
                                    <input type="text" name="sub_bridge_model_name" placeholder="Модель управляемого моста" value={carFilters.sub_bridge_model_name} onChange={handleCarFilterChange} />
                                    <input type="text" name="main_bridge_model_name" placeholder="Модель ведущего моста" value={carFilters.main_bridge_model_name} onChange={handleCarFilterChange} />
                                </div>
                                <div className="car-table-container">
                                    <table className="car-table info-table">
                                        <thead>
                                        <tr>
                                            <th>Заводской номер</th>
                                            <th>Модель машины</th>
                                            <th>Модель двигателя</th>
                                            <th>Номер двигателя</th>
                                            <th>Модель трансмиссии</th>
                                            <th>Номер трансмиссии</th>
                                            <th>Модель ведущего моста</th>
                                            <th>Номер ведущего моста</th>
                                            <th>Модель управляемого моста</th>
                                            <th>Номер управляемого моста</th>
                                            <th>Номер/дата договора</th>
                                            <th>Дата отгрузки</th>
                                            <th>Получатель</th>
                                            <th>Адрес</th>
                                            <th>Комплектация</th>
                                            <th>Владелец</th>
                                            <th>Сервисная компания</th>
                                        </tr>
                                        </thead>
                                        <tbody>
                                        {filteredCars.map(car => (
                                            <tr key={car.id}>
                                                <td><Link to={`/car/${car.id}`}>{car.car_number}</Link></td>
                                                <td><Link to={`/description/car-model/${car.car_model_id}`}>{car.car_model_name}</Link></td>
                                                <td><Link to={`/description/engine-model/${car.engine_model_id}`}>{car.engine_model_name}</Link></td>
                                                <td>{car.engine_number}</td>
                                                <td><Link to={`/description/transmission-model/${car.trans_model_id}`}>{car.trans_model_name}</Link></td>
                                                <td>{car.trans_number}</td>
                                                <td><Link to={`/description/main-bridge-model/${car.main_bridge_model_id}`}>{car.main_bridge_model_name}</Link></td>
                                                <td>{car.main_bridge_number}</td>
                                                <td><Link to={`/description/sub-bridge-model/${car.sub_bridge_model_id}`}>{car.sub_bridge_model_name}</Link></td>
                                                <td>{car.sub_bridge_number}</td>
                                                <td>{car.contract_number_date}</td>
                                                <td>{car.send_date}</td>
                                                <td>{car.receiver}</td>
                                                <td>{car.address}</td>
                                                <td>{car.equipment}</td>
                                                <td>{car.user}</td>
                                                <td>{car.service_company}</td>
                                            </tr>
                                        ))}
                                        </tbody>
                                    </table>
                                </div>
                            </>
                        )}
                        {activeTab === 'to' && (
                            <>
                                <div className="filters">
                                    <input type="text" name="type" placeholder="Вид ТО" value={maintenanceFilters.type} onChange={handleMaintenanceFilterChange} />
                                    <input type="text" name="car_number" placeholder="Зав. номер машины" value={maintenanceFilters.car_number} onChange={handleMaintenanceFilterChange} />
                                    <input type="text" name="service_company" placeholder="Сервисная компания" value={maintenanceFilters.service_company} onChange={handleMaintenanceFilterChange} />
                                </div>
                                <div className="car-table-container">
                                    <table className="car-table to-table">
                                        <thead>
                                        <tr>
                                            <th>Вид ТО</th>
                                            <th>Дата ТО</th>
                                            <th>Наработка, м/час</th>
                                            <th>Номер заказа-наряда</th>
                                            <th>Дата заказа-наряда</th>
                                            <th>Зав. номер машины</th>
                                            <th>Сервисная компания</th>
                                        </tr>
                                        </thead>
                                        <tbody>
                                        {filteredMaintenances.map(maintenance => (
                                            <tr key={maintenance.id}>
                                                <td>{maintenance.type.name}</td>
                                                <td>{maintenance.maintenance_date}</td>
                                                <td>{maintenance.worked_for}</td>
                                                <td>{maintenance.order_number}</td>
                                                <td>{maintenance.order_date}</td>
                                                <td>{maintenance.car.car_number}</td>
                                                <td>{maintenance.service_company.username}</td>
                                            </tr>
                                        ))}
                                        </tbody>
                                    </table>
                                </div>
                            </>
                        )}
                        {activeTab === 'reclaims' && (
                            <>
                                <div className="filters">
                                    <input type="text" name="broke_place" placeholder="Узел отказа" value={reclaimFilters.broke_place} onChange={handleReclaimFilterChange} />
                                    <input type="text" name="restore_method" placeholder="Способ восстановления" value={reclaimFilters.restore_method} onChange={handleReclaimFilterChange} />
                                    <input type="text" name="service_company" placeholder="Сервисная компания" value={reclaimFilters.service_company} onChange={handleReclaimFilterChange} />
                                </div>
                                <div className="car-table-container">
                                    <table className="car-table reclaims-table">
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
                                            <th>Зав. номер машины</th>
                                            <th>Сервисная компания</th>
                                        </tr>
                                        </thead>
                                        <tbody>
                                        {filteredReclaims.map(reclaim => (
                                            <tr key={reclaim.id}>
                                                <td>{reclaim.broke_date}</td>
                                                <td>{reclaim.worked_for}</td>
                                                <td>{reclaim.broke_place.name}</td>
                                                <td>{reclaim.broke_description}</td>
                                                <td>{reclaim.restore_method.name}</td>
                                                <td>{reclaim.used_spare_parts}</td>
                                                <td>{reclaim.restore_date}</td>
                                                <td>{reclaim.downtime}</td>
                                                <td>{reclaim.car.car_number}</td>
                                                <td>{reclaim.service_company.username}</td>
                                            </tr>
                                        ))}
                                        </tbody>
                                    </table>
                                </div>
                            </>
                        )}
                    </>
                ) : (
                    <div className="main-search">
                        <input className="main-search-field" type="text" placeholder="Заводской номер" value={searchNumber} onChange={(e) => setSearchNumber(e.target.value)} />
                        <button className="main-search-button" onClick={handleSearch}>Поиск</button>
                    </div>
                )}
                {carData && (
                    <>
                        <p className="car-table-info">Информация о комплектации и технических характеристиках Вашей техники</p>
                        <div className="car-table-container">
                            <table className="car-table">
                                <thead>
                                <tr>
                                    <th>Поле</th>
                                    <th>Значение</th>
                                </tr>
                                </thead>
                                <tbody>
                                <tr><td>Заводской номер</td><td>{isAuthorizedForFull ? <Link to={`/car/${carData.id}`}>{carData.car_number}</Link> : carData.car_number}</td></tr>
                                <tr><td>Модель машины</td><td>{isAuthorizedForFull ? <Link to={`/description/car-model/${carData.car_model_id}`}>{carData.car_model_name}</Link> : carData.car_model_name}</td></tr>
                                <tr><td>Модель двигателя</td><td>{isAuthorizedForFull ? <Link to={`/description/engine-model/${carData.engine_model_id}`}>{carData.engine_model_name}</Link> : carData.engine_model_name}</td></tr>
                                <tr><td>Номер двигателя</td><td>{carData.engine_number}</td></tr>
                                <tr><td>Модель трансмиссии</td><td>{isAuthorizedForFull ? <Link to={`/description/transmission-model/${carData.trans_model_id}`}>{carData.trans_model_name}</Link> : carData.trans_model_name}</td></tr>
                                <tr><td>Номер трансмиссии</td><td>{carData.trans_number}</td></tr>
                                <tr><td>Модель ведущего моста</td><td>{isAuthorizedForFull ? <Link to={`/description/main-bridge-model/${carData.main_bridge_model_id}`}>{carData.main_bridge_model_name}</Link> : carData.main_bridge_model_name}</td></tr>
                                <tr><td>Номер ведущего моста</td><td>{carData.main_bridge_number}</td></tr>
                                <tr><td>Модель управляемого моста</td><td>{isAuthorizedForFull ? <Link to={`/description/sub-bridge-model/${carData.sub_bridge_model_id}`}>{carData.sub_bridge_model_name}</Link> : carData.sub_bridge_model_name}</td></tr>
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
                    </>
                )}
            </main>
            <Footer/>
        </>
    );
}

export default HomePage;