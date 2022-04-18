import React, { useState } from 'react'
import axios from 'axios'




function StudHomePage(props) {

  const [name] = useState(props.abc.FirstName + " " + props.abc.LastName);
  const [UpdateSubject, setUpdateSubject] = useState(false);
  const [choose, setchoose] = useState(false);
  const [Update, setUpdate] = useState('');
  const [Response, setResponse] = useState([]);
  const [SelectedSubjects, setSelectedSubjects] = useState([])
  const[loading, setloading] = useState(false);
  const[continuousLoading, setcontinuousLoading] = useState(false);
//   const [Manage, setManage] = useState(false);

  

  const listItems = Response.map((response)=>   
    <label><input type="checkbox" name={response.id} onChange={handleChange}/> {response.name}<br></br></label> 
  ); 


  function handleChange(event){
      var temp = SelectedSubjects;
      if(event.target.checked === false && temp.includes(event.target.name)){
        temp = temp.filter(item => item !== event.target.name)
      }
      if(event.target.checked && !(temp.includes(event.target.name)))
      {
        temp.push(event.target.name)
      }
      setSelectedSubjects(temp);     
  }


  function enroll(event)
  {
    
    axios.get('http://127.0.0.1:5000/student/enroll?id='+ props.abc.Sid+'&Action=enroll')
            .then(results => {
                setchoose(true);
                setResponse(results.data.Result)
                setUpdateSubject(true);
                          
            });
            
        event.preventDefault();
  }

  function Add(event)
  {
      console.log(SelectedSubjects)
      axios.post('http://127.0.0.1:5000/student/enroll',{

      SId: props.abc.Sid,
      SubId: SelectedSubjects
    });
    
  }

  // function Ta(event)
  // {
  //   axios.get('http://127.0.0.1:5000/ta/')
  // }

  function withdraw(event)
  {
    axios.get('http://127.0.0.1:5000/student/enroll?id='+ props.abc.Sid+'&Action=withdraw')
            .then(results => {
                setResponse(results.data.Result)
                setUpdateSubject(true);          
            });
            
        event.preventDefault();
  }

  function Delete(event)
  {
    console.log(SelectedSubjects)
      axios.delete('http://127.0.0.1:5000/student/enroll',{

      data :{
        SId: props.abc.Sid,
        SubId: SelectedSubjects
      },     
    });
  }


  return (
    <div>
      {UpdateSubject ? choose ?  <div>
        <h1>Select the Course To Enroll</h1>
        {listItems}
        <br></br>
        <button onClick={Add}>Enroll</button>
        </div>
        : <div>
        <h1>Select the Course To Withdraw</h1>
        {listItems}
        <br></br>
        
        <button onClick={Delete}>Withdraw</button>
        </div>

        :<div> <h1>Welcome {name}</h1>
        <br></br>
        <br></br>
        <button onClick={()=>setUpdate('update')}>Update Subject</button>
        {/* <button onClick={}>Book an Appointment</button> */}
        {/* <button onClick={setManage(true)}>Manage Booking</button> */}
        <br></br>
        <br></br>
        :<p>
        {Update === "update" && <button onClick={enroll}>Enroll</button>}
        {Update === "update" && <button onClick={withdraw}>Withdraw</button>}
        </p>
        </div>}
    </div>
  );

}

export default StudHomePage;
