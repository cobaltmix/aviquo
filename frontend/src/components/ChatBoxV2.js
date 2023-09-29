import React, { useState, useEffect } from "react";
import { w3cwebsocket as W3CWebSocket } from "websocket";
import Button from "@material-ui/core/Button";
import CssBaseline from "@material-ui/core/CssBaseline";
import TextField from "@material-ui/core/TextField";
import Container from "@material-ui/core/Container";
import Card from "@material-ui/core/Card";
import CardHeader from "@material-ui/core/CardHeader";
import Paper from "@material-ui/core/Paper";
import { withStyles } from "@material-ui/core/styles";

const useStyles = (theme) => ({
  submit: {
    margin: theme.spacing(3, 0, 2),
  },
});

const ChatBox = ({ classes }) => {
  const [filledForm, setFilledForm] = useState(true);
  const [messages, setMessages] = useState([]);
  const [value, setValue] = useState("");
  const [name, setName] = useState("Test User");
  const [room, setRoom] = useState("test");
  const client = new W3CWebSocket("ws://127.0.0.1:8000/ws/" + room + "/");

  const onButtonClicked = (e) => {
    client.send(
      JSON.stringify({
        type: "message",
        text: value,
        sender: name,
      })
    );
    setValue("");
    e.preventDefault();
  };

  useEffect(() => {
    client.onopen = () => {
      console.log("WebSocket Client Connected");
    };
    client.onmessage = (message) => {
      const dataFromServer = JSON.parse(message.data);

      console.log(dataFromServer);
      
      if (dataFromServer) {
        setMessages((prevMessages) => [
          ...prevMessages,
          {
            msg: dataFromServer.text,
            name: dataFromServer.sender,
          },
        ]);
      }
    };
  }, [room]);

  return (
    <Container component="main" maxWidth="xs">
      {filledForm ? (
        <div style={{ marginTop: 50 }}>
          Aviquo Help Chat
          <Paper
            style={{
              height: 500,
              maxHeight: 500,
              overflow: "auto",
              boxShadow: "none",
            }}
          >
            {messages.map((message, index) => (
              <div key={index}>
                <Card className={classes.root}>
                  <CardHeader title={message.name} subheader={message.msg} />
                </Card>
              </div>
            ))}
          </Paper>
          <form className={classes.form} noValidate onSubmit={onButtonClicked}>
            <TextField
              id="outlined-helperText"
              label="Write text"
              variant="outlined"
              value={value}
              fullWidth
              onChange={(e) => setValue(e.target.value)}
            />
            <Button
              type="submit"
              fullWidth
              variant="contained"
              color="primary"
              className={classes.submit}
            >
              Send Message
            </Button>
          </form>
        </div>
      ) : (
        <div>
          <CssBaseline />
          <div className={classes.paper}>
            <form
              className={classes.form}
              noValidate
              onSubmit={() => setFilledForm(true)}
            >
              <TextField
                variant="outlined"
                margin="normal"
                required
                fullWidth
                label="Aviquo Help Chat"
                name="Aviquo Help Chat"
                autoFocus
                value={room}
                onChange={(e) => setRoom(e.target.value)}
              />
              <TextField
                variant="outlined"
                margin="normal"
                required
                fullWidth
                name="sender"
                label="sender"
                type="sender"
                id="sender"
                value={name}
                onChange={(e) => setName(e.target.value)}
              />
              <Button
                type="submit"
                fullWidth
                variant="contained"
                color="primary"
                className={classes.submit}
              >
                Submit
              </Button>
            </form>
          </div>
        </div>
      )}
    </Container>
  );
};

export default withStyles(useStyles)(ChatBox);
