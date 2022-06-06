import { useState } from "react";
import axios from 'axios';

// Component that parses user input and sends POST request to backend
const DescriptionInput = (props) => {
    const [description, setDescription] = useState('');
    const handleSubmit = async (event) => {
        event.preventDefault();
        const response = await axios.post(`http://127.0.0.1:5000/predict`, {
            desc: description
        }, {
            headers: {
                'Content-Type': 'text/plain;charset=utf-8',
                "Access-Control-Allow-Origin": "*",
            }
        });
       props.setRetrieved(true);
       props.setTopics([].concat(response.data.topics));
    }
    // Render book description form
    return (
     <div>
         <form onSubmit={handleSubmit}>
            <h1>Book Description</h1>
            <textarea value={description} onChange={(event) => setDescription(event.target.value)} /> <br/>
            <input type='submit' value='Submit'/> 
         </form>
     </div>   
    );
}

export default DescriptionInput;