import Results from './Results';
import DescriptionInput from './DescriptionInput';
import { useState } from 'react';
function App() {
  const [retrieved, setRetrieved] = useState(false);
  const [topics, setTopics] = useState(null);
  return (
    <div className="App">
      {retrieved ? <Results topics={topics}/> : <DescriptionInput setRetrieved = {setRetrieved} setTopics = {setTopics}/>}
    </div>
  );
}

export default App;
