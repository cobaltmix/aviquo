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
      AWSs: [],
             // ... more AWS data,
      isEditModalOpen: false,
      selectedAWS: null,
    }
  }

  componentDidMount() {
    this.refreshList();
    // if(this.state.AWSs.length === 0) {
    //   console.log('here')
    //   this.handleAddEntry({
    //     "AWSname" : "__",
    //     "password" : "__",
    //     "date_joined" : "2016-12-12T12:12:00-05:00"
    //   });

    //   this.refreshList();
    // }
  }

  refreshList = () => {
    axios
      .get("/api/AWS/")
      .then((res) => this.setState({ AWSs: res.data }))
      .catch((err) => console.log(err));
  };

  toggleEditModal = () => {
    this.setState((prevState) => ({
      isEditModalOpen: !prevState.isEditModalOpen,
    }));
  };

  handleEdit = (AWS) => {
    this.toggleEditModal();
    this.setState({ selectedAWS: AWS });
  };

  handleAddEntry = (newAWS) => {
    axios
      .post(`/api/AWS/`, newAWS)
      .then((res) => {
        console.log(res);
      })
  }

  handleSaveEdit = (editedAWS) => {
    // Send a PUT request to update the AWS with the edited data
    // Replace the following with your actual API endpoint and logic
    console.log(editedAWS)
    axios
      .put(`/api/AWS/${editedAWS.id}/`, editedAWS)
      .then((res) => {
        // Handle successful edit
        console.log('AWS edited:', editedAWS);
        this.toggleEditModal();
        this.refreshList();
      })
      .catch((err) => console.error('Error editing AWS:', err));
  };

  handleDelete = (editedAWS) => {
    // Send a PUT request to update the AWS with the edited data
    // Replace the following with your actual API endpoint and logic
    axios
      .delete(`/api/AWS/${editedAWS.id}/`, editedAWS)
      .then((res) => {
        // Handle successful edit
        console.log('AWS deleted:', editedAWS);
        this.toggleEditModal();
        this.refreshList();
      })
      .catch((err) => console.error('Error deleting AWS:', err));
  };

  render() {
    const keys = this.state.AWSs.length > 0 ? Object.keys(this.state.AWSs[0]) : [];

    const generateColor = (index) => {
      const colors = ['#2196F3', '#4CAF50', '#FFC107', '#9C27B0', '#FF5722'];
      return colors[index % colors.length];
    };

    return (
      <div className="body">
        <h1>AWS Table</h1>
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
                {this.state.AWSs.map((AWS, AWSIndex) => (
                  <tr key={AWS.id}>
                    {keys.map((key, index) => (
                      <td
                        key={index}
                        className="custom-cell"
                        style={{ backgroundColor: generateColor(index) }}
                      >
                        {AWS[key]}
                      </td>
                    ))}

                    <td className="custom-cell custom-cell-edit">
                      <Button size="sm" onClick={() => this.handleEdit(AWS)}>
                        Modify
                      </Button>
                    </td>
                    <td className="custom-cell custom-cell-delete">
                      <Button size="sm" onClick={() => this.handleDelete(AWS)}>
                        Delete
                      </Button>
                    </td>

                  </tr>
                ))}
                {/* Additional row for creating a new entry */}
                <tr>
                  <td colSpan={keys.length + 2}>
                    <Button size="sm" onClick={() => this.handleEdit(this.state.AWSs[0])}>
                      Create New
                    </Button>
                  </td>
                </tr>
              </tbody>
            </Table>
          </div>
          {this.state.selectedAWS && (
            <EditModal
              isOpen={this.state.isEditModalOpen}
              toggle={this.toggleEditModal}
              AWS={this.state.selectedAWS}
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