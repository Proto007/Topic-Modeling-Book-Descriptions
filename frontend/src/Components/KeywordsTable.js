import React, { useEffect, useState } from 'react';
import { AgGridReact } from 'ag-grid-react';

import 'ag-grid-community/styles/ag-grid.css';
import 'ag-grid-community/styles/ag-theme-alpine.css';

const KeywordsTable = (props) => {
    const [rowData, setRowData] = useState([
       {'Topic #': "Topic 1", 'Top Keywords per Topic (sorted by frequency)': '...'},
       {'Topic #': "Topic 2", 'Top Keywords per Topic (sorted by frequency)': '...'},
       {'Topic #': "Topic 3", 'Top Keywords per Topic (sorted by frequency)': '...'},
       {'Topic #': "Topic 4", 'Top Keywords per Topic (sorted by frequency)': '...'},
       {'Topic #': "Topic 5", 'Top Keywords per Topic (sorted by frequency)': '...'},
       {'Topic #': "Topic 6", 'Top Keywords per Topic (sorted by frequency)': '...'},
       {'Topic #': "Topic 7", 'Top Keywords per Topic (sorted by frequency)': '...'},
       {'Topic #': "Topic 8", 'Top Keywords per Topic (sorted by frequency)': '...'},
       {'Topic #': "Topic 9", 'Top Keywords per Topic (sorted by frequency)': '...'},
       {'Topic #': "Topic 10", 'Top Keywords per Topic (sorted by frequency)': '...'},
       {'Topic #': "Topic 11", 'Top Keywords per Topic (sorted by frequency)': '...'},
       {'Topic #': "Topic 12", 'Top Keywords per Topic (sorted by frequency)': '...'},
       {'Topic #': "Topic 13", 'Top Keywords per Topic (sorted by frequency)': '...'},
       {'Topic #': "Topic 14", 'Top Keywords per Topic (sorted by frequency)': '...'},
       {'Topic #': "Topic 15", 'Top Keywords per Topic (sorted by frequency)': '...'}
   ]);
   
   const [columnDefs] = useState([
       { field: 'Topic #', resizable: true, width: 100, cellStyle: {'border-right-color': '#e2e2e2', 'border-bottom-color':'#e2e2e2', 'text-align': 'center'}},
       { field: 'Top Keywords per Topic (sorted by frequency)', resizable: true, width: 750, cellStyle: {'border-bottom-color': '#e2e2e2'}},
   ]);

   useEffect(()=>{
        if (props.topicWords.length === 15){
            setRowData([
                {'Topic #': "Topic 1", 'Top Keywords per Topic (sorted by frequency)': props.topicWords[0].join(', ')},
                {'Topic #': "Topic 2", 'Top Keywords per Topic (sorted by frequency)': props.topicWords[1].join(', ')},
                {'Topic #': "Topic 3", 'Top Keywords per Topic (sorted by frequency)': props.topicWords[2].join(', ')},
                {'Topic #': "Topic 4", 'Top Keywords per Topic (sorted by frequency)': props.topicWords[3].join(', ')},
                {'Topic #': "Topic 5", 'Top Keywords per Topic (sorted by frequency)': props.topicWords[4].join(', ')},
                {'Topic #': "Topic 6", 'Top Keywords per Topic (sorted by frequency)': props.topicWords[5].join(', ')},
                {'Topic #': "Topic 7", 'Top Keywords per Topic (sorted by frequency)': props.topicWords[6].join(', ')},
                {'Topic #': "Topic 8", 'Top Keywords per Topic (sorted by frequency)': props.topicWords[7].join(', ')},
                {'Topic #': "Topic 9", 'Top Keywords per Topic (sorted by frequency)': props.topicWords[8].join(', ')},
                {'Topic #': "Topic 10", 'Top Keywords per Topic (sorted by frequency)': props.topicWords[9].join(', ')},
                {'Topic #': "Topic 11", 'Top Keywords per Topic (sorted by frequency)': props.topicWords[10].join(', ')},
                {'Topic #': "Topic 12", 'Top Keywords per Topic (sorted by frequency)': props.topicWords[11].join(', ')},
                {'Topic #': "Topic 13", 'Top Keywords per Topic (sorted by frequency)': props.topicWords[12].join(', ')},
                {'Topic #': "Topic 14", 'Top Keywords per Topic (sorted by frequency)': props.topicWords[13].join(', ')},
                {'Topic #': "Topic 15", 'Top Keywords per Topic (sorted by frequency)': props.topicWords[14].join(', ')}
            ])
        }
    },[props.topicWords]);

   return (
       <div className="ag-theme-alpine-dark" style={{width:'95vh',height:'100.3vh'}}>
           <AgGridReact
               rowHeight={61}
               rowData={rowData}
               columnDefs={columnDefs}>
           </AgGridReact>
       </div>
   );
};

export default KeywordsTable;
