import { useState } from "react";


// Component that parses user input and sends POST request to backend
const DescriptionInput = (props) => {
    const [description, setDescription] = useState('');
    const handleSubmit = (event) => {
        event.preventDefault();
        /*
            API Call
        */
       props.setRetrieved(true);
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