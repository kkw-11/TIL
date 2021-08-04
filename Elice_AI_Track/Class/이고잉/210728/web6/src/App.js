
import './App.css';
function HeaderTag(props){
  return(
    <header>
      <h1>
      <a href="index.html">{props.title}</a>
      </h1>
    </header>
  )
}

function NavTag(props){
  console.log('props',props);
  var d = props.data;
  var lis = [];
  for(var i = 0; i<d.length; ++i){
    console.log(i, d[i]);
    lis.push(<li>{d[i].title}</li>);
  }
  return (
    <nav>
    <ul>
      {lis}
    </ul>
  </nav>
  );

}

function ArticleTag(props){
  return(
    <article>
      <h2>{props.title}</h2>
     {props.desctirption}
    </article>
  );
}

function App() {
  var topic = [
    {id:1, title:'html', desctirption:'html is ...'},
    {id:2, title:'css', desctirption:'css is ...'}
  ]
  return (
    <div className="App">
      <HeaderTag title = "I love Web"/>
      <NavTag data = {topic}/>
      <ArticleTag title = "Hello" desctirption = "hello react"/>
    </div>
  );
}

export default App;