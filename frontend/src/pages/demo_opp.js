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
    const [url, setUrl] = useState('/api/Opportunity/');
    const [title, setTitle] = useState('Opportunities');

    const { globalState } = useContext(GlobalContext);

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
            .then((res) => setUsers(res.data))
            .catch((err) => console.log(err));
    };

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
                "name": "",
                "description": "",
                "tags": []
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
            <h1>{title} Table</h1>
            <div className="body">
                <div className="table-container">
                    <Table responsive className="custom-table">
                        <thead>
                            <tr>
                                {keys.map((key, index) => (
                                    <th
                                        key={index}
                                        className="custom-header"
                                        style={{ backgroundColor: generateColor(index) }}
                                    >
                                        {key}
                                    </th>
                                ))}

                                <th className="custom-header">Edit</th>
                                <th className="custom-header">Delete</th>
                            </tr>
                        </thead>
                        <tbody>
                            {users.map((user, userIndex) => (
                                <tr key={user.id}>
                                    {keys.map((key, index) => (
                                        <td
                                            key={index}
                                            className="custom-cell"
                                            style={{ backgroundColor: generateColor(index) }}
                                        >
                                            {user[key]}
                                        </td>
                                    ))}

                                    <td className="custom-cell custom-cell-edit">
                                        <Button size="sm" onClick={() => handleEdit(user)}>
                                            Modify
                                        </Button>
                                    </td>
                                    <td className="custom-cell custom-cell-delete">
                                        <Button size="sm" onClick={() => handleDelete(user)}>
                                            Delete
                                        </Button>
                                    </td>

                                </tr>
                            ))}
                            {/* Additional row for creating a new entry */}
                            <tr>
                                <td colSpan={keys.length + 2}>
                                    <Button size="sm" onClick={() => handleAdd(users[0])}>
                                        Create New
                                    </Button>
                                </td>
                            </tr>
                        </tbody>
                    </Table>
                </div>
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