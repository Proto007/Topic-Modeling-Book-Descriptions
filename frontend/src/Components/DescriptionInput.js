import { useState } from "react";
import Introduction from "./Introduction";

// Component that parses user input and sends POST request to backend
const DescriptionInput = (props) => {
    const [description, setDescription] = useState('');
    const handleSubmit = async (event) => {
        event.preventDefault();
        const response = await fetch(`http://127.0.0.1:3000/predict`, {
            method: 'POST', 
            headers: {
              'Content-Type': 'text/plain;charset=utf-8'
            },
            body: description
          })
        console.log(response);
        props.setTopics([].concat(response.body.topics));
        props.setRetrieved(true);
    }
    // Render book description form
    return (
     <div style={ {
      // Try setting `flexDirection` to `"row"`.
      display:"flex",
      flexDirection: "row",
      justifyContent:"flex-start"
    }}>
         <Introduction/>
         <form onSubmit={handleSubmit}>
            <textarea placeholder="Enter a book description..." rows="28" cols="60" value={description} onChange={(event) => setDescription(event.target.value)} style={{fontSize:"20pt",marginLeft:"2px"}}/> <br/>
            <input type='submit' value='Get Topics' style={{width:'95vh',height:'6.8vh', background:"#000000",color:"white", marginLeft:"2px",fontSize:"20pt", fontFamily:"cursive",padding:"10px 25px",cursor:"pointer"}}/> 
         </form>
     </div>   
    );
}

export default DescriptionInput;