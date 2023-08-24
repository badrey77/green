import { Flex, HStack, Image, List, ListItem, Text, UnorderedList } from "@chakra-ui/react";
import SearchResultsItem from "./SearchResultsItem";
import { FoodDataStruct } from "../utils/types";


const ResultsList = ({ foods }) => {

    const elements: Array<FoodDataStruct> = foods;
    
    return (
        <List>
            <Flex>
            { elements.map(elem=>(
                <SearchResultsItem key={elem.food.foodId} { ... elem } />
            )) }
            </Flex>
        </List>
    )
    
}

export default ResultsList;