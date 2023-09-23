import React, { Component } from 'react';
import { Modal, ModalHeader, ModalBody, ModalFooter, Button } from 'reactstrap';

class EditModal extends Component {
  constructor(props) {
    super(props);
    this.state = {
      editedUser: JSON.parse(JSON.stringify(props.user)),
    };
  }

  // handleInputChange = (e) => {
  //   const { name, value } = e.target;
  //   this.setState((prevState) => ({
  //     editedUser: { ...prevState.editedUser, [name]: value },
  //   }));
  // };

  handleInputChange = (e) => {
    const { name, value } = e.target;
    this.setState((prevState) => ({
      editedUser: { ...prevState.editedUser, [name]: value },
    }));
    
  };

  handleSave = () => {
    const { editedUser } = this.state;
    this.props.onSave(editedUser);
  };

  

  render() {
    const [ isOpen, toggle, editedUser ] = [ this.props.isOpen, this.props.toggle, this.props.user ];

    return (
      <Modal isOpen={isOpen}  centered>
        <ModalHeader>Edit User</ModalHeader>
        <ModalBody>
          <form>
            {Object.keys(editedUser).map((key, index) => (
              <div className="form-group" key={index}>
                <label>{key}</label>
                <input
                  type="text"
                  className="form-control"
                  name={key}
                  defaultValue={editedUser[key] !== null ? editedUser[key] : ''}
                  onChange={this.handleInputChange}
                />
              </div>
            ))}
          </form>
        </ModalBody>
        <ModalFooter>
          <Button color="primary" onClick={this.handleSave}>
            Save
          </Button>
          <Button color="secondary" onClick={toggle}>
            Cancel
          </Button>
        </ModalFooter>
      </Modal>
    );
  }
}

export default EditModal;