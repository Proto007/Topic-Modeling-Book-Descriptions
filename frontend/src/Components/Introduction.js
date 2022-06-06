import Results from "./Results";

const Introduction =() => {
    return (
        <div style={{height:'90vh', width:'50%', padding:'50px', backgroundColor:'#000000',fontFamily:'monospace',fontSize:'25px',color:'#FFFFFF'}}>
            <Results></Results>
            <h2>Topic Modeling Book Descriptions</h2>
            <div style={{textAlign:"justify"}}>
                Latent Dirichlet Allocation is an unsupervised machine learning algorithm that allows topic modeling. A topic model is a statistical model for discovering the abstract "topics" that occur in a collection of documents.This simple application demonstrates a topic model using a book description dataset. The lda model contains 15 abstract topics that are generated based on provided roughly 7000 book descriptions. Each “topic” is a collection of words that are frequent for that particular topic. The model gives probability of a given description being within each of the 15 topics predicted by the model.
            </div>
            <img src="lda.png" alt="algorithm" style={{padding:"50px 2px",height:"45vh",width:"90vh"}}></img>
        </div>
    );
}
export default Introduction;