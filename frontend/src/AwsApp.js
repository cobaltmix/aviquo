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
      Awss: [
        { id: 1, Awsname: 'john_doe', first_name: 'John', last_name: 'Doe', email: 'john@example.com' },
        { id: 2, Awsname: 'jane_doe', first_name: 'Jane', last_name: 'Doe', email: 'jane@example.com' },
        // ... more Aws data
      ],
      isEditModalOpen: false,
      selectedAws: null,
    }
  }

  componentDidMount() {
    this.refreshList();
  }

  refreshList = () => {
    axios
      .get("/api/AWS")
      .then((res) => this.setState({ Awss: res.data }))
      .catch((err) => console.log(err));
  };

  toggleEditModal = () => {
    this.setState((prevState) => ({
      isEditModalOpen: !prevState.isEditModalOpen,
    }));
  };

  handleEdit = (Aws) => {
    this.setState({ selectedAws: Aws });
    this.toggleEditModal();
  };

  handleSaveEdit = (editedAws) => {
    // Send a PUT request to update the Aws with the edited data
    // Replace the following with your actual API endpoint and logic
    axios
      .put(`/api/AWS/${editedAws.id}/`, editedAws)
      .then((res) => {
        // Handle successful edit
        console.log('Aws edited:', editedAws);
        this.toggleEditModal();
        this.refreshList();
      })
      .catch((err) => console.error('Error editing Aws:', err));
  };

  render() {
    const keys = this.state.Awss.length > 0 ? Object.keys(this.state.Awss[0]) : [];


    const generateColor = (index) => {
      const colors = ['#2196F3', '#4CAF50', '#FFC107', '#9C27B0', '#FF5722'];
      return colors[index % colors.length];
    };

    const handleDelete = (Aws) => {
      console.log('Delete button clicked for Aws ID:', Aws.id);
    };

    return (
      <div className="body">
        <h1>Aws Table</h1>
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
                {this.state.Awss.map((Aws, AwsIndex) => (
                  <tr key={Aws.id}>
                    {keys.map((key, index) => (
                      <td
                        key={index}
                        className="custom-cell"
                        style={{ backgroundColor: generateColor(index) }}
                      >
                        {Aws[key]}
                      </td>
                    ))}
                    <td className="custom-cell custom-cell-edit">
                      <Button size="sm" onClick={() => this.handleEdit(Aws)}>
                        Modify
                      </Button>
                    </td>
                    <td className="custom-cell custom-cell-delete">
                      <Button size="sm" onClick={() => handleDelete(Aws)}>
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
            Aws={this.state.selectedAws}
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
