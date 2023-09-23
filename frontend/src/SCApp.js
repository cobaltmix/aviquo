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
      SCs: [
        { id: 1, SCname: 'john_doe', first_name: 'John', last_name: 'Doe', email: 'john@example.com' },
        { id: 2, SCname: 'jane_doe', first_name: 'Jane', last_name: 'Doe', email: 'jane@example.com' },
        // ... more SC data
      ],
      isEditModalOpen: false,
      selectedSC: null,
    }
  }

  componentDidMount() {
    this.refreshList();
  }

  refreshList = () => {
    axios
      .get("/api/SC")
      .then((res) => this.setState({ SCs: res.data }))
      .catch((err) => console.log(err));
  };

  toggleEditModal = () => {
    this.setState((prevState) => ({
      isEditModalOpen: !prevState.isEditModalOpen,
    }));
  };

  handleEdit = (SC) => {
    this.setState({ selectedSC: SC });
    this.toggleEditModal();
  };

  handleSaveEdit = (editedSC) => {
    // Send a PUT request to update the SC with the edited data
    // Replace the following with your actual API endpoint and logic
    axios
      .put(`/api/SC/${editedSC.id}/`, editedSC)
      .then((res) => {
        // Handle successful edit
        console.log('SC edited:', editedSC);
        this.toggleEditModal();
        this.refreshList();
      })
      .catch((err) => console.error('Error editing SC:', err));
  };

  render() {
    const keys = this.state.SCs.length > 0 ? Object.keys(this.state.SCs[0]) : [];


    const generateColor = (index) => {
      const colors = ['#2196F3', '#4CAF50', '#FFC107', '#9C27B0', '#FF5722'];
      return colors[index % colors.length];
    };

    const handleDelete = (SC) => {
      console.log('Delete button clicked for SC ID:', SC.id);
    };

    return (
      <div className="body">
        <h1>SC Table</h1>
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
                {this.state.SCs.map((SC, SCIndex) => (
                  <tr key={SC.id}>
                    {keys.map((key, index) => (
                      <td
                        key={index}
                        className="custom-cell"
                        style={{ backgroundColor: generateColor(index) }}
                      >
                        {SC[key]}
                      </td>
                    ))}
                    <td className="custom-cell custom-cell-edit">
                      <Button size="sm" onClick={() => this.handleEdit(SC)}>
                        Modify
                      </Button>
                    </td>
                    <td className="custom-cell custom-cell-delete">
                      <Button size="sm" onClick={() => handleDelete(SC)}>
                        Delete
                      </Button>
                    </td>
                  </tr>
                ))}
              </tbody>
            </Table>


          </div>
          {this.state.selectedEC && (
          <EditModal
            isOpen={this.state.isEditModalOpen}
            toggle={this.toggleEditModal}
            SC={this.state.selectedSC}
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
