import { useState } from "react";

const DescriptionInput = (props) => {
    const [description, setDescription] = useState('');
    const handleSubmit = (event) => {
        event.preventDefault();
        /*
            API Call
        */
       props.setRetrieved(true);
    }
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