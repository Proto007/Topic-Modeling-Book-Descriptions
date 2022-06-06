import { useState } from "react";
import axios from 'axios';

// Component that parses user input and sends POST request to backend
const DescriptionInput = (props) => {
    const [description, setDescription] = useState('');
    const handleSubmit = async (event) => {
        event.preventDefault();
        const response = await axios.post(`${window.location.host}:5000/classify`, {
            desc: description
        });
       props.setRetrieved(true);
       props.setTopics([].concat(response.data.topics));
       props.setProbabilities([].concat(response.data.probabilities));
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