import React, { Component } from 'react';
import { Modal, ModalHeader, ModalBody, ModalFooter, Button } from 'reactstrap';

class EditModal extends Component {
  constructor(props) {
    super(props);
    this.state = {
      editedUser: { ...props.user },
    };
  }

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
    const { isOpen, toggle, user, onSave, editedUser, handleInputChange } = this.props;

    return (
      <Modal isOpen={isOpen} toggle={toggle} centered>
        <ModalHeader toggle={toggle}>Edit User</ModalHeader>
        <ModalBody>
          <form>
            {Object.keys(editedUser).map((key, index) => (
              <div className="form-group" key={index}>
                <label>{key}</label>
                <input
                  type="text"
                  className="form-control"
                  name={key}
                  value={editedUser[key] !== null ? editedUser[key] : ''}
                  onChange={handleInputChange}
                />
              </div>
            ))}
          </form>
        </ModalBody>
        <ModalFooter>
          <Button color="primary" onClick={() => onSave(editedUser)}>
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
