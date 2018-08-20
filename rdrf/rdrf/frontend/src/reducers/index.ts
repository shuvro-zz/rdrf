import { combineReducers } from 'redux';
import promsPageReducer from '../pages/proms_page/reducers';

const rootReducer = combineReducers({
    promsPage: promsPageReducer,
});

export default rootReducer;