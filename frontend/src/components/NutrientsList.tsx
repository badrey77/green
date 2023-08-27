import { Box, Flex, List, Stack } from "@chakra-ui/react";
import NutrientsListItem from "./NutrientsListItem";
import { FoodDataStruct } from "../utils/types";


const NutrientsList = ({ foods }) => {

    const elements: Array<FoodDataStruct> = foods;
    
    return (
        <Stack>
            { elements.map(elem=>(
                <NutrientsListItem { ... elem } />
            )) }      
        </Stack>
    )
    
}

export default NutrientsList;