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
      ECs: [],
             // ... more EC data,
      isEditModalOpen: false,
      selectedEC: null,
    }
  }

  componentDidMount() {
    this.refreshList();
    // if(this.state.ECs.length === 0) {
    //   console.log('here')
    //   this.handleAddEntry({
    //     "ECname" : "__",
    //     "password" : "__",
    //     "date_joined" : "2016-12-12T12:12:00-05:00"
    //   });

    //   this.refreshList();
    // }
  }

  refreshList = () => {
    axios
      .get("/api/ECS/")
      .then((res) => this.setState({ ECs: res.data }))
      .catch((err) => console.log(err));
  };

  toggleEditModal = () => {
    this.setState((prevState) => ({
      isEditModalOpen: !prevState.isEditModalOpen,
    }));
  };

  handleEdit = (EC) => {
    this.toggleEditModal();
    this.setState({ selectedEC: EC });
  };

  handleAddEntry = (newEC) => {
    axios
      .post(`/api/EC/`, newEC)
      .then((res) => {
        console.log(res);
      })
  }

  handleSaveEdit = (editedEC) => {
    // Send a PUT request to update the EC with the edited data
    // Replace the following with your actual API endpoint and logic
    console.log(editedEC)
    axios
      .put(`/api/ECS/${editedEC.id}/`, editedEC)
      .then((res) => {
        // Handle successful edit
        console.log('EC edited:', editedEC);
        this.toggleEditModal();
        this.refreshList();
      })
      .catch((err) => console.error('Error editing EC:', err));
  };

  handleDelete = (editedEC) => {
    // Send a PUT request to update the EC with the edited data
    // Replace the following with your actual API endpoint and logic
    axios
      .delete(`/api/ECS/${editedEC.id}/`, editedEC)
      .then((res) => {
        // Handle successful edit
        console.log('EC deleted:', editedEC);
        this.toggleEditModal();
        this.refreshList();
      })
      .catch((err) => console.error('Error deleting EC:', err));
  };

  render() {
    const keys = this.state.ECs.length > 0 ? Object.keys(this.state.ECs[0]) : [];

    const generateColor = (index) => {
      const colors = ['#2196F3', '#4CAF50', '#FFC107', '#9C27B0', '#FF5722'];
      return colors[index % colors.length];
    };

    return (
      <div className="body">
        <h1>EC Table</h1>
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
                {this.state.ECs.map((EC, ECIndex) => (
                  <tr key={EC.id}>
                    {keys.map((key, index) => (
                      <td
                        key={index}
                        className="custom-cell"
                        style={{ backgroundColor: generateColor(index) }}
                      >
                        {EC[key]}
                      </td>
                    ))}

                    <td className="custom-cell custom-cell-edit">
                      <Button size="sm" onClick={() => this.handleEdit(EC)}>
                        Modify
                      </Button>
                    </td>
                    <td className="custom-cell custom-cell-delete">
                      <Button size="sm" onClick={() => this.handleDelete(EC)}>
                        Delete
                      </Button>
                    </td>

                  </tr>
                ))}
                {/* Additional row for creating a new entry */}
                <tr>
                  <td colSpan={keys.length + 2}>
                    <Button size="sm" onClick={() => this.handleEdit(this.state.ECs[0])}>
                      Create New
                    </Button>
                  </td>
                </tr>
              </tbody>
            </Table>
          </div>
          {this.state.selectedEC && (
            <EditModal
              isOpen={this.state.isEditModalOpen}
              toggle={this.toggleEditModal}
              EC={this.state.selectedEC}
              onSave={this.handleSaveEdit}
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