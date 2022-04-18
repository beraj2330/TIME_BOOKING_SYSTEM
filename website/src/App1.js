import React from 'react'; 

class App1 extends React.Component {
  constructor(props) {
    super(props);
    this.state = { id: '', email: ''};
  }
  mySubmitHandler = (event) => {
    event.preventDefault();
    alert("You are submitting " + this.state.id +" "+ this.state.email);
  }
  myChangeId = (event) => {
    this.setState({id: event.target.value});
  }

  myChangeEmail = (event) =>{
    this.setState({email: event.target.value});
  }


  
  render() {
    return (
      <form onSubmit={this.mySubmitHandler}>
      
      <label for="id">Id:</label>
      <input
        type="text"
        onChange={this.myChangeId}
      />
      <br></br>

      <label for="email">Email:</label>
      <input
        type="email"
      
        onChange={this.myChangeEmail}
      />
      <br></br>

      <input 
        type="submit"
        value="Log In"
        />      
      </form>
      
    );
  }
}
export default App1;