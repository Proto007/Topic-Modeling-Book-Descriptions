const Introduction =() => {
    return (
        <div style={{height:'90vh', width:'50%', padding:'50px', backgroundColor:'#000000',fontFamily:'monospace',fontSize:'25px',textAlign:'justify',color:'#FFFFFF'}}>
            <h2>Topic Modeling Book Descriptions</h2>
            Latent Dirichlet Allocation is an unsupervised machine learning algorithm that allows topic modeling. A topic model is a statistical model for discovering the abstract "topics" that occur in a collection of documents.This simple application demonstrates a topic model using a book description dataset. The lda model contains 15 abstract topics that are generated based on provided roughly 7000 book descriptions. Each “topic” is a collection of words that are frequent for that perticular topic. The model gives probability of a given description being within each of the 15 topics predicted by the model.
        </div>
    );
}
export default Introduction;