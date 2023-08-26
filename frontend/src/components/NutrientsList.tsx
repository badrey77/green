import { Flex, HStack, Image, List, ListItem, Text, UnorderedList } from "@chakra-ui/react";
import NutrientsListItem from "./NutrientsListItem";
import { FoodDataStruct } from "../utils/types";


const NutrientsList = ({ foods }) => {

    const elements: Array<FoodDataStruct> = foods;
    
    return (
        <List>
            <Flex>
            { elements.map(elem=>(
                <NutrientsListItem key={elem.food.foodId} { ... elem } />
            )) }
            </Flex>
        </List>
    )
    
}

export default NutrientsList;