// import logo from './logo.svg';
import './App.css';
import EditModal from './EditModal';
import axios from "axios";
import { Table, Button } from 'reactstrap';
import React, { Component } from 'react';

class App extends Component {
  constructor(props) {
    super(props)
    this.state = {
      users: [],
             // ... more user data,
      isEditModalOpen: false,
      selectedUser: null,
      selectedAdd: null, 
      url: '',
      title: ''
    }
    this.state.url = this.props.url
    this.state.title = this.props.title
  }

  componentDidMount() {
    this.refreshList();
    // if(this.state.users.length === 0) {
    //   console.log('here')
    //   this.handleAddEntry({
    //     "username" : "__",
    //     "password" : "__",
    //     "date_joined" : "2016-12-12T12:12:00-05:00"
    //   });

    //   this.refreshList();
    // }
  }

  refreshList = () => {
    axios
      .get(this.state.url)
      .then((res) => this.setState({ users: res.data }))
      .catch((err) => console.log(err));
  };

  toggleEditModal = () => {
    this.setState((prevState) => ({
      isEditModalOpen: !prevState.isEditModalOpen,
    }));
  };

  handleEdit = (user) => {
    this.toggleEditModal();
    this.setState({ selectedUser: user });
  };


  handleAddEntry = (addedUser) => {

    console.log(addedUser)
    
    axios
      .post(`${this.state.url}`, addedUser)
      .then((res) => {
        // Handle successful addition
        console.log('User edited:', addedUser);
        this.toggleEditModal();
        this.refreshList();
      })
      .catch((err) => console.error('Error adding user:', err));
  };
  
  
  handleAdd = () => {
    console.log('dummy')
    this.toggleEditModal();
    this.setState({ selectedAdd: {
    "id": "3",
    "password": "",
    "last_login": null,
    "is_superuser": false,
    "username": "",
    "first_name": "",
    "last_name": "",
    "email": "",
    "is_staff": false,
    "is_active": true,
    "date_joined": "2023-09-24T10:40:32.765545-04:00",
    "groups": [],
    "user_permissions": [],}
  });
  };


  handleSaveEdit = (editedUser) => {
    // Send a PUT request to update the user with the edited data
    // Replace the following with your actual API endpoint and logic
    console.log(editedUser)
    axios
      .put(`${this.state.url}${editedUser.id}/`, editedUser)
      .then((res) => {
        // Handle successful edit
        console.log('User edited:', editedUser);
        this.toggleEditModal();
        this.refreshList();
      })
      .catch((err) => console.error('Error editing user:', err));
  };

  handleDelete = (editedUser) => {
    // Send a PUT request to update the user with the edited data
    // Replace the following with your actual API endpoint and logic
    axios
      .delete(`${this.state.url}${editedUser.id}/`, editedUser)
      .then((res) => {
        // Handle successful edit
        console.log('User deleted:', editedUser);
        this.toggleEditModal();
        this.refreshList();
      })
      .catch((err) => console.error('Error deleting user:', err));
  };

  render() {
    const keys = this.state.users.length > 0 ? Object.keys(this.state.users[0]) : [];

    const generateColor = (index) => {
      const colors = ['#2196F3', '#4CAF50', '#FFC107', '#9C27B0', '#FF5722'];
      return colors[index % colors.length];
    };

    return (
      <div className="body">
        <h1>{this.state.title}</h1>
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
                {this.state.users.map((user, userIndex) => (
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
                      <Button size="sm" onClick={() => this.handleEdit(user)}>
                        Modify
                      </Button>
                    </td>
                    <td className="custom-cell custom-cell-delete">
                    <Button size="sm" onClick={() => this.handleAddEntry()}>
                        Delete
                      </Button>
                    </td>

                  </tr>
                ))}
                {/* Additional row for creating a new entry */}
                <tr>
                  <td colSpan={keys.length + 2}>
                    <Button size="sm" onClick={() => this.handleAdd(this.state.users[0])}>
                      Create New
                    </Button>
                  </td>
                </tr>
              </tbody>
            </Table>
          </div>
          {this.state.selectedUser && (
            <EditModal
              isOpen={this.state.isEditModalOpen}
              toggle={this.toggleEditModal}
              user={this.state.selectedUser}
              onSave={this.handleSaveEdit}
            />
          )}
          {this.state.selectedAdd && (
            <EditModal
              isOpen={this.state.isEditModalOpen}
              toggle={this.toggleEditModal}
              user={this.state.selectedAdd}
              onSave={this.handleAddEntry}
            />
          )}
        </div>
      </div>
    );
  }




}
// function App() {
//   return (
//     <div className="App">
//       <header className="App-header">
//         <img src={logo} className="App-logo" alt="logo" />
//         <p>
//           Edit <code>src/App.js</code> and save to reload.
//         </p>
//         <a
//           className="App-link"
//           href="https://reactjs.org"
//           target="_blank"
//           rel="noopener noreferrer"
//         >
//           Learn React
//         </a>
//       </header>
//     </div>
//   );
// }


export default App;