interface RegionData {
    [region: string]: {
        [viewDate: string] : {
            technologies: {
                [key: string]: number
            },
            totalCount: number;
        };
    }
}

interface SelectedRegion {
    [region: string]: {
        [viewDate: string]: {
            technologies: {
                [key:string]:number
            },
            totalCount: number;
        }
    } & {
        id: string; 
        totalCountAll: number;
    }
}

interface TechnologyData {
    [date: string] : {},
    technology: string
}
export interface PageState {
    modalOpen: boolean,
    sidebarOpen: boolean,
    regionDataAll?: RegionData[],
    viewTechnology: string,
    viewDate: string,
    selectedRegion?: SelectedRegion,
    selectedRegionID?: string,
    technologyDataAll?: TechnologyData[]
}

export enum ActionTypes {
    openModal = 'OPEN_MODAL',
    closeModal = 'CLOSE_MODAL',
    toggleModal = 'TOGGLE_MODAL',
    toggleSidebar = 'TOGGLE_SIDEBAR',
    regionData = 'REGION_DATA',
    viewTechnology = 'VIEW_TECHNOLOGY',
    viewDate = 'VIEW_DATE',
    selectRegion = 'SELECT_REGION',
    selectRegionID = 'SELECT_REGION_ID',
    technologyData = 'TECHNOLOGY_DATA'
}

interface PageAction {
    type: ActionTypes;
    payload? : any;
    id?: string;
}

export const pageReducer = (state: PageState, action: PageAction) => {
    switch(action.type) {
        case ActionTypes.openModal: {
            return {
                ...state,
                modalOpen: true
            }
        } case ActionTypes.closeModal: {
            return {
                ...state,
                modalOpen: false
            }
        } case ActionTypes.toggleModal: {
            return {
                ...state,
                modalOpen: !state.modalOpen
            }
        } case ActionTypes.toggleSidebar: {
            return {
                ...state,
                sidebarOpen: !state.sidebarOpen
            }
        } case ActionTypes.regionData: {
            return {
                ...state,
                regionDataAll: action.payload
            }
        } case ActionTypes.viewDate: {
            return {
                ...state,
                viewDate: action.payload
            }
        } case ActionTypes.viewTechnology: {
            return {
                ...state,
                viewTechnology: action.payload
            }
        } case ActionTypes.selectRegion: {
            return {
                ...state,
                selectedRegion: action.payload
            }
        } case ActionTypes.selectRegionID: {
            return {
                ...state,
                selectedRegionID: action.id
            }
        } case ActionTypes.technologyData: {
            return {
                ...state,
                technologyDataAll: action.payload
            }
        }
        default: return state;
    }
}