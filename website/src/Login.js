import React, { useState } from 'react'
import axios from 'axios'
import StudHomePage from './StudentHomePage'

function Login() {
    const [id, setId] = useState("1");
    const [email, setEmail] = useState("jeelbera2330@gmail.com");
    const [student, setStudent] = useState();
    const [Role, setRole] = useState();
    const [showMessage, setShowMessage] = useState(false);
    


    function login(event) {
        axios.get('http://127.0.0.1:5000/student?Sid=' + id + '&email=' + email)
            .then(resp => {
                setStudent(resp.data)
                setShowMessage(true)
                setRole(resp.data.Role)
            });
            
            event.preventDefault();
    }
    return (

        <div>
            { showMessage ? <StudHomePage abc={student} />
            
              : <div>
                <h1>Login Page</h1>
                <br /><br/>
                <form onSubmit={login}>

                <label htmlFor="id">Id:</label>
                <input
                    type="text"
                    placeholder="id"    
                    onChange={(e) => setId(e.target.value)}
                />
                <br></br>
                <br></br>

                <label htmlFor="email">Email:</label>
                <input
                    type="email"
                    placeholder="email"
                    onChange={(e) => setEmail(e.target.value)}
                />
                <br></br>
                <br></br>
                <button type="submit" >Login</button>
            </form>
             </div>}

        </div>


    )
}

export default Login;