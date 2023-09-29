import '../deprecated/App.css';
import EditModal from '../deprecated/EditModal';
import { Table, Button } from 'reactstrap';
import { GlobalContext } from '../GlobalContext';
import React, { Component, useState, useEffect, useContext } from 'react';
import axios from 'axios';


const Demo = () => {
    const { updateGlobalState } = useContext(GlobalContext);
    const getApiKeyFromLocalStorage = () => {
        const apiKey = localStorage.getItem('api_key');
        if (apiKey) {
            console.log(apiKey)
            updateGlobalState({
                api_key: apiKey,
            });
        }
    };

    useEffect(() => {
        getApiKeyFromLocalStorage();
     }, []);
    const [users, setUsers] = useState([]);
    const [isEditModalOpen, setIsEditModalOpen] = useState(false);
    const [isAddModalOpen, setIsAddModalOpen] = useState(false);
    const [selectedUser, setSelectedUser] = useState(null);
    const [selectedAdd, setSelectedAdd] = useState(null);
    const [url, setUrl] = useState('/api/Waitlist/');
    const [title, setTitle] = useState('Waitlist');

    const { globalState } = useContext(GlobalContext);
    var userCount = null
    
    useEffect(() => {
        refreshList();
        // eslint-disable-next-line react-hooks/exhaustive-deps
    }, []);

    const refreshList = () => {
        axios
            .get(url, {
                headers : {
                    'x-api-key': globalState.api_key,
                }
            })
            .then((res) => refreshFunc(res.data))
            .catch((err) => console.log(err));
    };  
    const [buttonText, setButtonText] = useState('Click');
    function refreshFunc(data) {
        setUsers(data)
        console.log(data.length)
        userCount = data.length
        setButtonText(userCount);
    }

    const toggleEditModal = () => {
        setIsEditModalOpen((prevState) => !prevState);
    };

    const toggleAddModal = () => {
        setIsAddModalOpen((prevState) => !prevState);
    };

    const handleEdit = (user) => {
        toggleEditModal();
        setSelectedUser(user);
    };

    const handleAddEntry = (addedUser) => {
        console.log(globalState.api_key);
        addedUser.tags = Array(1,2,3)
        console.log(addedUser)

        axios
            .post(url, addedUser, {
                headers : {
                    'x-api-key': globalState.api_key,
                }
            })
            .then((res) => {
                console.log('User edited:', addedUser);
                toggleAddModal();
                refreshList();
            })
            .catch((err) => console.log(err));
    };

    const handleAdd = () => {
        toggleAddModal();
        setSelectedAdd(
            {
                "email": "",
                "date_created": ""
            }
        );

    };

    const handleSaveEdit = (editedUser) => {
        console.log(globalState.api_key);
      
        axios
            .put(`${url}${editedUser.id}/`, editedUser, {
                headers : {
                    'x-api-key': globalState.api_key,
                }
            })
            .then((res) => {
                console.log('User edited:', editedUser);
                toggleEditModal();
                refreshList();
            })
            .catch((err) => console.log(err));
    };

    const handleDelete = async (editedUser) => {
        try {
            const response = await axios.delete(`${url}${editedUser.id}/`, {
                headers: {
                    'x-api-key': globalState.api_key,
                }
            });

            console.log('User deleted:', editedUser);
            refreshList();
        } catch (error) {
            console.error('Error deleting user:', error);
        };
    }
    const keys = users.length > 0 ? Object.keys(users[0]) : [];

    const generateColor = (index) => {
        const colors = ['#2196F3', '#4CAF50', '#FFC107', '#9C27B0', '#FF5722'];
        return colors[index % colors.length];
    };

    return (
        <div className="body">
             <h1>User count in waitlist: {buttonText}</h1>
            <div className="body">
              
                {selectedUser && (
                    <EditModal
                        isOpen={isEditModalOpen}
                        toggle={toggleEditModal}
                        user={selectedUser}
                        onSave={handleSaveEdit}
                    />
                )}
                {selectedAdd && (
                    <EditModal
                        isOpen={isAddModalOpen}
                        toggle={toggleAddModal}
                        user={selectedAdd}
                        onSave={handleAddEntry}
                    />
                )}
            </div>
        </div>
    );
};

export default Demo;