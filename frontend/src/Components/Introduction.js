import Results from "./Results";

const Introduction =(props) => {
    return (
        <div style={{height:'100vh', width:'50vw', padding:'5vh', backgroundColor:'#000000',fontFamily:'monospace', color:'#FFFFFF'}}>
            <h2 style={{textAlign:"justify", fontSize:"2vw", textOverflow: "ellipsis"}}>Topic Modeling Book Descriptions</h2>
            <div style={{textAlign:"justify", fontSize:"1.25vw"}}>
                Latent Dirichlet Allocation is an unsupervised machine learning algorithm that allows topic modeling. A topic model is a statistical model for discovering the abstract "topics" that occur in a collection of documents.This simple application demonstrates a topic model using a book description dataset. The lda model contains 15 abstract topics that are generated based on provided roughly 7000 book descriptions. Each “topic” is a collection of words that are frequent for that particular topic. The model gives probability of a given description being within each of the 15 topics predicted by the model.
            </div>
            {props.correlations.length === 15 ? (
                <Results topicWords={props.topicWords} correlations={props.correlations}></Results>
            ):(
                <img src="lda.png" alt="algorithm" style={{padding:"50px 2px",height:"45%",width:"100%"}}></img>
            )}
        </div>
    );
}

export default Introduction;
