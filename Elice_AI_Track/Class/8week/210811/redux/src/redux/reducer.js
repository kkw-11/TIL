const initState = {
    count = 0,


}



const Reducer = {
    (state = initState, action) =>{
        switch(action.type){
            case "INCREMENT":
                return {
                    count: state.count + 1
                }
            default:
                return state;

        }
    }
}

export defalut Reducer; 